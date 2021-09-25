from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


class BlogPostsView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})


class PostView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title',
        'content'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    fields = [
        'title',
        'content'
    ]
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
