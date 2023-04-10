from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'main/home.html', context)