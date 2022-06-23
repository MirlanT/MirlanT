
from django.urls import path
from webapp.views import index_app, index_create,article_view


urlpatterns = [
    path('', index_app),
    path('articles/add/', index_create),
    path('articles/', article_view)
]