from django.shortcuts import render
from second_app.models import User

# Create your views here.
def index(request):
    user_list = User.objects.order_by('first_name')
    return render(request, 'second_app/index.html',context={'user_list': user_list})
