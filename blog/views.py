from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from blog.models import Post


def post_list(request):
    """docstring for post_list"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
