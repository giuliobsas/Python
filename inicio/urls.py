from django.urls import path
from inicio.views import vista, vista2, vista3, inicio, vista4, vista5, template1, template2, cliente, buscar_producto
app_name = 'inicio'

urlpatterns = [   
    path('vista/', vista, name='vista'),
    path('vista2/', vista2, name='vista2'),
    path('vista3/', vista3, name='vista3'), 
    path('', inicio, name='inicio'),  
    path('vista4/', vista4, name='vista4'), 
    path('vista5/<nombre>/', vista5, name='vista5'),
    path('template1/', template1, name='template1'),
    path('template2/', template2, name='template2'),
    path('cliente/', cliente, name='cliente'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
]


