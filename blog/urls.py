from django.conf.urls import include, url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.post_list),
    path('index/' ,views.index, name="index"),
    path('qsomos/' ,views.qsomos, name="qsomos"),
    path('fundacion/' ,views.fundacion, name="fundacion"),
    path('formulario/' ,views.formulario, name="formulario"),
    path('galeria/' ,views.galeria, name="galeria"),
    path('inicio/' ,views.inicio, name="inicio"),
]
