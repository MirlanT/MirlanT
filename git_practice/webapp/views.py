from django.shortcuts import render

# Create your views here.
from webapp.models import Article


def index_app(request):
    articles = Article.objects.order_by("-created_at")
    contex = {"articles": articles}
    return render(request, 'index.html', contex)


def index_create(requeste):
    if requeste.method == "GET":
        return render(requeste, 'create.html')
    else:
        contex = {
            'title': requeste.POST.aget("title"),
            'author': requeste.POST.get("author"),
            'content': requeste.POST.get("content")

        }
        return render(requeste, 'create.html')
