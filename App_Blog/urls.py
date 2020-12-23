from django.urls import path
from . import views

app_name = 'App_Blog'
urlpatterns= [
    path('',views.BlogListView.as_view(),name='blog_list'),
    path('write',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<slug:slug>',views.blog_details.as_view(),name='blog_list'),
    path('liked/<pk>',views.liked.as_view(),name='liked_post'),
    path('unliked/<pk>',views.unliked.as_view(),name='unliked_post'),
    path('my-blog/',views.MyBlogs.as_view(),name='my_blogs'),
    path('edit-blog/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'),
]