from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def docs(request):
    return render(request, 'mainapp/doc.html')
    
def labs(request):
    return render(request, 'mainapp/labs.html')