from django.shortcuts import render
from .models import Post, Comment

#Index Posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

# individual post w/ associated comments
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})

def comment_list(request):
    comments = Comment.objects.all()
    return render (request, 'scribble/comment_list.html', {'comments': comments})