from django.urls import path,include
from . import views
app_name = 'mecanicos'
urlpatterns = [
 path("cadastrar",views.cadastro_mecanico,name="cadastrar"),
 path("equipe",views.cadastro_equipe,name="cadastrar_equipe"),
]
