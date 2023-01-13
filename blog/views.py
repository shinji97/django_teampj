from django.shortcuts import render
from .models import Post

def mg_page(request):
    return render(
        request,
        'blog/jangmaga.html',

    )

def gw_page(request):
    return render(
        request,
        'blog/gwangwon.html',

    )

def sj_page(request):
    return render(
        request,
        'blog/sujin.html',

    )

def je_page(request):
    return render(
        request,
        'blog/shinji.html',

    )

def sy_page(request):
    return render(
        request,
        'blog/seoyeon.html',

    )

def single_post_page(request, value):
    post = Post.objects.get(pk=value)
    return render(
        request,
        'blog/single_post_page.html',

    {
        'post' : post,
    }
    )

    
def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
    'blog/index.html', 
    {
        'posts': posts
    }
    )

# Create your views here.