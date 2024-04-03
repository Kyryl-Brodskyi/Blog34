from django import forms
from .models import Post, PostPhoto, Comment, Subscriber, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

PhotoFormSet = forms.inlineformset_factory(Post, PostPhoto, fields=('image', 'description'), extra=3)


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'user')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PostPhoto
        fields = ('image', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']