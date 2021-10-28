from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .models import Author,Book
from .forms import AuthorForm, BookForm

def index(request):
    return render(request, 'model_forms/index.html')

def author_form_view(request):
    if request.method == 'POST':
        # Create a form instance with POST data.
        a = Author()
        f = AuthorForm(request.POST, instance=a)

        # Create and save the new author instance. There's no need to do anything else.
        new_author = f.save()
        print(new_author)
        return HttpResponseRedirect('/modelforms/author')
    else:
        f = AuthorForm()
    return render(request,'model_forms/model_form_one.html', context={'authorForm':f})

def book_form_view(request):
    if request.method == 'POST':
        # Create a form instance with POST data.
        a = Book()
        f = BookForm(request.POST, instance=a)

        # Create and save the new author instance. There's no need to do anything else.
        new_book = f.save()
        print(new_book)
        return HttpResponseRedirect('/modelforms/book')

    else:
        f = BookForm()
    return render(request,'model_forms/model_form_two.html', context={'bookForm':f})
