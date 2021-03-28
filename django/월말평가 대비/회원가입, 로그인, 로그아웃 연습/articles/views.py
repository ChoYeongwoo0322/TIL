from django.shortcuts import render,redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe  

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles":articles,
    }
    return render(request, "articles/index.html", context)

@login_required
def create(request):
    if request.method =="POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm()
    context={
        "form":form,
    }
    return render(request, "articles/create.html", context)

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
        }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", pk)
    else:
        form = ArticleForm(instance=article)
    context={
        "form":form,
        "article":article,
    }
    return render(request, "articles/update.html", context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =="POST":
        article.delete()
        return redirect("articles:index")
    return redirect("articles:detail", article.pk)


def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('articles:detail', article.pk)

@login_required
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)