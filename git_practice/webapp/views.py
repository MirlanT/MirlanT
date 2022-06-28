from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from webapp.models import Article
from webapp.models import STATUS_CH


def index_app(request):
    articles = Article.objects.order_by("-created_at")
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
        # return HttpResponseRedirect(reverse("article_view", kwargs={"pk": new_article.pk}))
        # return HttpResponseRedirect(f"/articles/{new_article.pk}")
