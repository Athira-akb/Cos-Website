from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'webpage/base.html')

def home(request):
    return render(request,'webpage/home.html')

