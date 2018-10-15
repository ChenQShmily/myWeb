from django.shortcuts import render
from .models import Post
# trips/views.py

from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate,login,logout


def welcome(request):
    web_list = Post.objects.all()
    return render(request, 'welcome.html', {'web_list': web_list})

def newsContent(request, pk):
    content = Post.objects.get(pk=pk)
    return render(request, 'content.html', {'content': content})

def newsDelete(request, pk):
    content = Post.objects.get(pk=pk)
    content.delete()
    web_list = Post.objects.all()
    return render(request, 'welcome.html', {'web_list': web_list})



def log_in(request):
    print(request.method)
    if request.method == "POST": 
        input_name = request.POST['name']
        input_pwd = request.POST['pwd']
        user = authenticate(username=input_name,password=input_pwd)
        if user and user.is_active:
            login(request,user)
            web_list = Post.objects.all()
            return render(request, 'welcome.html', {'web_list': web_list})
        else:
            return render(request, 'login.html',{'status':'ERROR Incorrect username or password'}) 
 
    return render(request,'login.html')

def log_out(request):
    logout(request)
    web_list = Post.objects.all()
    return render(request, 'welcome.html', {'web_list': web_list})
