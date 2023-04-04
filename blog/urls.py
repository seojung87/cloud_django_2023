from django.urls import path
from . import views

urlpatterns = [
    #path('<int:post_num>/', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    #path('', views.index),
    path('', views.PostList.as_view()),
    path('category/<str:slug>/', views.categories_page),
    path('tags/<str:slug>/', views.tag_page),
]