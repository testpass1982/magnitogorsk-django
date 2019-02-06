from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def docs(request):
    return render(request, 'mainapp/doc.html')
    
def laboratoriya(request):
    return render(request, 'mainapp/laboratoriya.html')