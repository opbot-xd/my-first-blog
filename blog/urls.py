from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_article_list'),
    path('post/<int:pk>/', views.post_detail, name='post_article_detail'),
    path('post/new/', views.post_new , name='post_new_article'),
    path('post/<int:pk>/edit/', views.post_edit, name='update_article'),
]