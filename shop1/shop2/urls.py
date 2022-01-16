from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import HomeView, ArticleDetailView, AddCommentView,  AboutView,ContactView
from django.contrib.auth import views as auth_views




urlpatterns = [
   path('', HomeView, name="home"),
   path('about', AboutView, name="about"),
   path('contact', ContactView, name="contact"),
   path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
   path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
]