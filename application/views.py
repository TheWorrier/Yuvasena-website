from django.shortcuts import render,HttpResponse

# Create your views here.
def application(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')
