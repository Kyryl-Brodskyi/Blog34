from django.urls import path
from .views import user_logout
from .import views
from django.contrib.auth.views import LoginView
from .views import create_post
from .views import profile
from .views import update_profile
from .views import registration_user


urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>", views.post, name="post"),
    path("post/<int:post_id>/add_comment", views.add_comment, name="add_comment"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path('category/<str:name>', views.category, name="category"),
    path("search", views.search, name="search"),
    path("create", create_post, name="create"),
    path("subscribe", views.subscribe, name="subscribe"),
    path("success", views.success_page, name="success_page"),
    path("login", LoginView.as_view(), name="blog_login"),
    path('logout', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register/', registration_user, name='register'),
]