from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'client/accueil.html')
def handler404(request):
    return render(request, '404.html')