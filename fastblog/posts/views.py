from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from posts.models import Post



def post_comments(request, pk):
    post = Post.objects.get(pk=pk)
    comment = post.comment_set.create(
        content=request.POST.get("content"),
    )

    return redirect(post)
