from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django_bongo import settings
from .models import *


# Create your views here.
@login_required(login_url="/receipe/login")
def receipe_home(request):
    print(settings.BASE_DIR)
    if request.POST:
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        # print(receipe_name +" and desc is: "+ receipe_description+' and image: '+receipe_image)
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect("/receipe")
    queryset = Receipe.objects.all()
    context = {"receipes": queryset}
    return render(request, "receipes/receipe.html", context=context)


def delete_receipe(request, id):
    queryset = Receipe.objects.all(id=id)
    queryset.delete()
    return redirect("/receipe")


def login_page(request):
    if request.POST:
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        if not User.objects.filter(username=username).exists():
            print(username + " exists")
            return render(request, "login.html")
        user = authenticate(username=username, password=password)
        if user is None:
            print(username + " authenticated")
            return render(request, "login.html")
        else:
            login(request, user)
            return redirect("/receipe")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/receipe/login")


def register(request):
    if request.POST:
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("user_name")
        password = data.get("password")
        print(first_name + last_name + password + username)

        user = User.objects.filter(username=username)
        if user.exists():
            return render(request, "register.html")
        else:
            user = User.objects.create(
                first_name=first_name, last_name=last_name, username=username
            )
            user.set_password(password)
            user.save()
    return render(request, "register.html")
