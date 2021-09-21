from django.urls import path
from . import views
from .views import BlogPostsView, PostView, CreatePostView, EditPostView, DeletePostView

urlpatterns = [
    path('', BlogPostsView.as_view(template_name='blogs/home.html'), name='index'),
    path('post/<int:pk>/', PostView.as_view(template_name='blogs/post.html'), name='post'),
    path('post/new/', CreatePostView.as_view(), name='new_post'),
    path('post/<int:pk>/edit', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('about/', views.about, name='about'),
]
