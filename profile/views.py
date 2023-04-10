from django.shortcuts import render, HttpResponse

# Create your views here.

def profile(request, pk):
    context = {}
    return render(request, 'profile/home.html', context)