from django.shortcuts import render
from django.views import generic
from .models import Post
# from django.http import HttpResponse

# Create your views here.
# def my_blog(request):
#     return HttpResponse("Hello, Blog!")

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("-created_on")
    template_name = "post_list.html"
