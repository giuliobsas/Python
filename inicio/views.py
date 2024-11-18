from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context 

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

def vista5(request, nombre):
    nombre = nombre.upper()
    return HttpResponse(f'Hola mundo en la aplicacion <h1>INICIO</h1> y lo hizo {nombre}')

def template1(request):
    
    template_archivo = open(r'templates\template1.html')
    
    template = Template(template_archivo.read())
    
    
    template_archivo.close()
    
    contexto = Context()
    
    #template armado con el context para que sea entendido por el html
    templateRender = template.render(contexto)
    
    return HttpResponse(templateRender)



