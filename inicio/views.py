from django.shortcuts import render
from django.http import HttpResponse

def vista(request):
    return HttpResponse('Hola mundo')

def vista2(request):
    return HttpResponse('Hola mundo2')

def vista3(request):
    return HttpResponse('Hola mundo3')

def inicio(reqeust):
    return HttpResponse('inicio')

def vista4(request):
    return HttpResponse('Hola mundo4')

def vista5(request):
    return HttpResponse('Hola mundo en la aplicacion <h1>INICIO</h1>')

