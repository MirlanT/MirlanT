from django.urls import path
from webapp.views import index_app, index_create, article_view, main_view

urlpatterns = [
    path('', main_view, name='main'),
    path('art/', index_app, name="index"),
    path('articles/add/', index_create, name="article_add"),
    path('articles/<int:pk>/', article_view, name="article_view")
]
