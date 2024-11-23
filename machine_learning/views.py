from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def machine(request):
    return render (request,'index.html')

def deep_learning(request):
    return HttpResponse('Welcome to Django Deep learning')
def about(request):
    return HttpResponse('Welcome to Django about')
