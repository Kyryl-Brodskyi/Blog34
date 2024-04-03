from django.contrib.auth import logout as django_logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Category, Comment, Tag, PostPhoto, Profile
from .forms import PostForm, CommentForm, SubscriptionForm, UserProfileForm, RegistrationForm, PhotoFormSet, AvatarForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_categories():
    all_categories = Category.objects.all()
    count = all_categories.count()
    half = count // 2 + count % 2
    return {'cats1': all_categories[:half], 'cats2': all_categories[half:]}


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def post(request, post_id=None):
    post = get_object_or_404(Post, id=post_id)
    images = PostPhoto.objects.filter(post=post)
    tags = post.tags.all()
    comments = post.comments.all()
    context = {
        "post": post,
        "images": images,
        "tags": tags,
        "comments": comments,
    }
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def about(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def contact(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/contact.html', context)


def category(request, name=None):
    category_obj = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=category_obj).order_by("-published_date")
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        author = request.user.username
        text = request.POST.get('comment_text')
        if text:
            comment = Comment.objects.create(post=post, author=author, text=text)
            comment.save()

            tag1, created1 = Tag.objects.get_or_create(name='Tag1')
            tag2, created2 = Tag.objects.get_or_create(name='Tag2')

            post.tags.add(tag1, tag2)
    return redirect('post', post_id=post_id)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__contains=query))
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        formset = PhotoFormSet(request.POST, request.FILES)
        if post_form.is_valid() and formset.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            formset.instance = post
            formset.save()
            return redirect('post', post_id=post.pk)
    else:
        post_form = PostForm()
        formset = PhotoFormSet()
    return render(request, 'blog/create.html', {'post_form': post_form, 'formset': formset})


@login_required
def add_comment_to_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = SubscriptionForm()
    return render(request, 'blog/subscribe.html', {'form': form})


def success_page(request):
    return render(request, 'blog/success_page.html')


def user_logout(request):
    django_logout(request)
    return redirect("index")


def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarForm(instance=profile)
    return render(request, 'blog/profile.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blog/update_profile.html', {'form': form})


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'blog/registration_user.html', {'form': form})


