from django.shortcuts import render
from django.http import HttpResponse
import random
import string



def home(request):
    return render(request, "generator/home.html")

def password(request):

    characters=list(string.ascii_lowercase)

    if request.GET.get("верхний регистр"):
        characters.extend(string.ascii_uppercase)

    if request.GET.get("особые знаки"):
        characters.extend(list("!@#*%$()"))

    if request.GET.get("цифры"):
        characters.extend(list([str(x) for x in range(10)]))

    length = int(request.GET.get("длина пароля",12))

    thepassword = ""
    for x in range(length):
        thepassword+= random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})

