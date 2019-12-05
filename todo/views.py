from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView 
from django.contrib.auth.forms import UserCreationForm  
from django.urls import reverse_lazy 
from . import forms
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post


class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "todo/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "todo/logout.html"

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-importance','-published_date')
    form = PostForm()
    return render(request, 'todo/index.html', {'posts': posts, 'form': form})

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "todo/create.html"
    success_url = reverse_lazy("login")

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.consumer = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

def important_rank(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.importance += 1
    post.save()
    return redirect('index')














    
