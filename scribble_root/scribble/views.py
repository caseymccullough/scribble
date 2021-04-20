from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Index
# New
# Destroy
# Update
# Create
# Edit
# Show

#Index Posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts}) # posts: posts is a key value pair

#Index Comments
def comment_list(request):
    comments = Comment.objects.all()
    return render (request, 'scribble/comment_list.html', {'comments': comments})

#New Post
def post_create(request):
    if request.method == "POST":
        #create a form instance and populate with data
        form = PostForm(request.POST)
        #check whether it's valid
        if form.is_valid():
            #Save new post and redirect to show page
            post = form.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'scribble/post_form.html', {'form': form})


#New Comment
def comment_create(request):
    if request.method == "POST":
        #create a comment instance and populate with data
        form = CommentForm(request.POST)
        #check whether it's valid
        if form.is_valid():
            #Save new post and redirect to show page
            comment = form.save()
            # there is no comment detail, so go to associated post.  
            # !! valid syntax?
            return redirect('post_detail', pk = comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'scribble/comment_form.html', {'form': form})

# Destroy a Post
def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    # back to post list page 
    return redirect('post_list')

# Destroy a Comment
def comment_delete(request, pk):
    post_pk = Comment.objects.get(id=pk).post.id
    Comment.objects.get(id=pk).delete()
    # back to post list page 
    ## !! change to current post? 
    return redirect('post_detail', pk = post_pk)

# Update / Edit Post
def post_edit (request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save() # data now from form prev from db
            return redirect('post_detail', pk=post.pk)
    else: # they are requesting to get the form
        form = PostForm(instance = post) # populate with current data
    return render(request, 'scribble/post_form.html', {'form': form})

# Update / Edit Comment
def comment_edit (request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        # populate form with current data
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save() # data now from form prev from db
            return redirect('post_detail', pk=comment.post.pk)
    else: # they are requesting to get the form
        form = CommentForm(instance = comment) # populate with current data
    return render(request, 'scribble/comment_form.html', {'form': form})

# Show individual post w/ associated comments
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})

# Show individual comment
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'scribble/comment_detail.html', {'comment': comment})
