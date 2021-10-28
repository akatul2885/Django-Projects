from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'forms/index.html', context={'message':'Hello from form index'})

def form_comment_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        commentForm = forms.CommentForm(request.POST)
        # check where it's valid
        if commentForm.is_valid():
            data = commentForm.cleaned_data
            print(data)
            # redirecting to new URL:
            return HttpResponseRedirect('/basicforms')
    # if a GET or any other request then we will create a blank form
    else:
         commentForm = forms.CommentForm()

    return render(request, 'forms/form_page.html', context={'commentFrom':commentForm})

