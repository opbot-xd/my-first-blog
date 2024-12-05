from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_article_list(request):
    '''Provides a list of articles published.'''
    postings =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':postings})

def post_article_detail(request, pk):
    '''Displays article details.'''
    post_on_click = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post_on_click})

def post_new_article(request):
    '''Posts new article.'''
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def update_article(request, article_id):
  """Edits an existing article."""
  article = get_object_or_404(Post, pk=article_id)
  if request.method == "POST":
    edit_form = PostForm(request.POST, instance=article)
    if edit_form.is_valid():
      edited_article = edit_form.save(commit=False)
      edited_article.author = request.user
      edited_article.published_date = timezone.now()
      edited_article.save()
      return redirect('post_detail', pk=edited_article.pk)
  else:
    edit_form = PostForm(instance=article)
  return render(request, 'blog/post_edit.html', {'edit_form': edit_form})
