from django.urls import path,include
from . import views
app_name = 'clientes'
urlpatterns = [
 path("cadastrar",views.cadastro_cliente,name="cadastrar"),
]