from django.shortcuts import render


# Create your views here.
def index_view(requeste):
    if requeste.method == "GET":
        return render(requeste, 'index.html')
    else:
        contex = {
            'title': requeste.POST.get("title"),
            'author': requeste.POST.get("author"),
            'content': requeste.POST.get("content")

        }
        return render(requeste, 'index.html')
