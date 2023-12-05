
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/',include('usuarios.urls')),
    path('mecanico/',include('mecanicos.urls')),
    path('cliente/',include('clientes.urls')),
    path('servicos/',include('servicos.urls')),
]
