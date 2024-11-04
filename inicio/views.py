from django.http import HttpResponse

def vista(request):
    return HttpResponse('Hola mundo')

def inicio(request):
    return HttpResponse('<h1>Soy la pagina de inicio</h1>')