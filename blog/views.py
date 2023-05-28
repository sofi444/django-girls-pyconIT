from django.shortcuts import render
from .models import Post # dot means current dir
from django.utils import timezone

# Create your views here.

def post_list(request):
    # QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 
                  'blog/post_list.html', # path to template file
                  {'posts': posts})