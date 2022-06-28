
from django.urls import path
from webapp.views import index_app, index_create,article_view


urlpatterns = [
    path('', index_app, name="index"),
    path('articles/add/', index_create, name="article_add"),
    path('articles/<int:pk>/', article_view, name="article_view")
]