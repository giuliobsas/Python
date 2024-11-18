from django.http import HttpResponse

def vista(request):
    return HttpResponse('Hola mundo')
