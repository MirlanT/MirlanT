
from django.urls import path
from webapp.views import index_app, index_create

urlpatterns = [
    path('', index_app),
    path('article/add', index_create)
]