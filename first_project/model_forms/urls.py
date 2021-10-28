from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('author',views.author_form_view, name='authorForm'),
    path('book',views.book_form_view, name='bookForm')
]