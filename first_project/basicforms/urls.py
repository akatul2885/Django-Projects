from django.urls import path
from . import views
# Create your views here.
urlpatterns=[
    path('', views.index, name="index"),
    path('form_one', views.form_comment_view, name="form")
]
