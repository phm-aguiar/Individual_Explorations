from django.shortcuts import render
# Create your views here.

def blog(request):
    print('Hello, World!')
    return render(request, "blog/index.html")

def images(request):
    ...
