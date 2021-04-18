from .models import Post, Comment

#Index Posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

def post_detail(request):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.get(post=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})