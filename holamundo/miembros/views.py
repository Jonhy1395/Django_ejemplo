from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

def index(request):
    return HttpResponse("Hola, mundo")

def new(request):
    print("Mathod: ",request.method)
    if request.method == 'POST':
        return HttpResponse("Esta registrando datos.")
    else:
        return HttpResponseNotAllowed(["POST"],"Metodo invalido")

def read(request):
    if request.method == 'GET':
        return HttpResponse("Esta consultando datos")
    else:
        return HttpResponseNotAllowed(["GET"],"Metodo invalido")


