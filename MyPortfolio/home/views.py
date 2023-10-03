from django.shortcuts import render
from django.http import HttpResponse

app_name = 'home'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def VDD(request):
    return render(request, 'VDD.html')