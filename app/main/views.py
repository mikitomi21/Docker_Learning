from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MessageForm

# Create your views here.

def home(request):
    form = MessageForm()
    if request.method == "POST":
        print(request.POST.get('description'))
        form = MessageForm(request.POST)
        if form.is_valid() and request.POST.get('description'):
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'main/home.html', context)

def about(request):
    return HttpResponse("Halo halo")