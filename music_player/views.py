from django.shortcuts import render


def home(request):
    return render(request, 'home.html') #一切开始的地方


