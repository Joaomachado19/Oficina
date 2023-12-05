from django.urls import path,include
from . import views
app_name = 'servicos'
urlpatterns = [
 path("cadastrar/ordem_de_servico",views.cadastro_ordem,name="ordem_de_servico"),
]