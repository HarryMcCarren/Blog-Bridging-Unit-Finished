from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from blog.models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required


# Create your views here.
class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

@login_required
@permission_required('post.add')
def post_new(request):
    if (request.method == "POST"):
        form = PostForm(request.POST);
        if (form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.id);
    else:
        form = PostForm()
        return render(request, "blog/post_edit.html",
        {"form": form})

@login_required
@permission_required('post.change')
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if (request.method == "POST"):
        form = PostForm(request.POST, instance=post);
        if (form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail",pk=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})

@login_required
def add_comment_to_post(request, id):
    post = get_object_or_404(Post, id=id);
    if (request.method == "POST"):
        form = CommentForm(request.POST)
        if (form.is_valid()):
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.id);
    else:
        form = CommentForm();
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
@permission_required('comment.can_approve')
def comment_approve(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.approve()
    return redirect("post_detail", pk=comment.post.id)

@login_required
@permission_required('comment.delete')
def comment_remove(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("post_detail", pk=comment.post.id)

@login_required
@permission_required('post.can_see_drafts')
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True)
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
@permission_required('post.can_publish')
def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    post.publish()
    return redirect("post_detail", pk=id)

@login_required
@permission_required('post.delete')
def post_remove(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("post_list")

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if (request.method == "POST"):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, "Account created"
            +" successfully.")
            return redirect("post_list");
    else:
        form = UserCreationForm()
        return render(request, "signup.html", 
        {"form":form})

def about_me(request):
	return render(request, 'about_me.html')
def projects(request):
	return render(request, 'projects.html')