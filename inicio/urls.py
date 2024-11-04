from django.urls import path
from inicio.views import vista, inicio

urlpatterns = [
    path('Vista/', vista),
    path('', inicio)
]
