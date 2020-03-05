from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)  
from .models import Post 


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


#https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #ordering the posts from newest to oldest

class PostDetailView(DetailView):
    model = Post


#LoginRequiredMixin = if you try to access the '/post/new' url & the correct user is not logged in - it will show the LoginPage
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
                'cork', 'kerry', 'dublin', 'limerick', 'meath', 'waterford', 
                'boiler_installations', 'heating_control_installations', 'boiler_and_heating_control_installations']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
                'cork', 'kerry', 'dublin', 'limerick', 'meath', 'waterford', 
                'boiler_installations', 'heating_control_installations', 'boiler_and_heating_control_installations']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #ensuring that the author of the post is the only person allowed to update that post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
 