from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   
	return render(request, 'Empresa/index.html')

def produtos(request):
   
    return render(request, 'Empresa/produtos.html')

def lajetreliçada(request):
   
    return render(request, 'Empresa/lajeTre.html')

def lajecovencional(request):
    
    return render(request, 'Empresa/Lajecovencional.html')

def lajebidirecional(request):
   
    return render(request, 'Empresa/bidirecional.html')

def postes(request):
    
    return render(request, 'Empresa/postes.html')

def pingadeira(request):
   
    return render(request, 'Empresa/pingadeira.html')

def eps(request):
    
    return render(request, 'Empresa/eps.html')

def contato(request):
   
    return render(request, 'Empresa/Contato.html')


def empresa(request):
    
    return render(request, 'Empresa/empresa.html')


def galeria(request):
    
    return render(request, 'Empresa/galeria.html')







