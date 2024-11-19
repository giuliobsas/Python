from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader 
from datetime import datetime   


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

def template2(request):
    
    fecha_actual = datetime.now()
    fecha = {
        "Fecha": fecha_actual,
        'numeros': list(range(1,11)),
        }
         

    # template_archivo = open(r'templates\template2.html')
    
    # template = Template(template_archivo.read())
    
    # template_archivo.close()

    # contexto = Context()
    
    # #template armado con el context para que sea entendido por el html
    # templateRender = template.render(contexto)
    
    #V2
    # template = loader.get_template('template2.html')
    # # contexto = Context(fecha_actual) el loader automaticamente genera el contexto. ESTO NO VA PERO ESTA OCULTO.
    # templateRender = template.render(fecha)
    
    # return HttpResponse(templateRender)

    #V3
    # ya no utilizamos el Httpresponse
    # en esta version ya no necesitamos especificar cada detalle del template. 
    # Para los proximos templates utilizamos toda la version 3. 
    return render(request, 'template2.html', fecha)

# def cliente(request, nombre, marca, color):
    
#     dato = cliente(nombre=nombre, marca=marca, color=color)
#     dato.save()
#     return render(request, 'cliente.html', {'dato': dato})
# NO HAY URL CONFIG


