from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from webapp.models import Article
from webapp.models import STATUS_CH


def index_app(request):
    articles = Article.objects.order_by("-updated_at")
    contex = {"articles": articles}
    return render(request, 'index.html', contex)


def main_view(request):
    return render(request, 'main.html')


def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    contex = {
        "article": article
    }
    return render(request, 'article.html', contex)


def index_create(request):
    if request.method == "GET":
        contex = {
            "statuses": STATUS_CH
        }
        return render(request, 'create.html', contex)
    else:
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        status = request.POST.get("status")
        date = request.POST.get("date")
        if not date:
            date = None
        new_article = Article.objects.create(title=title, author=author, content=content, status=status, date=date)
        # contex = {
        #     "article": new_article
        # }
        return redirect("article_view", pk=new_article.pk)

def index_update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "GET":
        contex = {
            "statuses": STATUS_CH,
            "article": article
        }
        return render(request, 'update.html', contex)
    else:
        article.title = request.POST.get("title")
        article.author = request.POST.get("author")
        article.content = request.POST.get("content")
        article.status = request.POST.get("status")
        article.date = request.POST.get("date")
        if not article.date:
            article.date = None
        article.save()
        return redirect("article_view", pk=article.pk)


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"article": article})
    else:
        article.delete()
        return redirect("index")
