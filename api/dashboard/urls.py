from django.conf.urls import url, include

from .views import *

urlpatterns =[
    url(r'^usuarios/$', crearUsuario ),
    url(r'^canales/$', canales),
    url(r'^canales/(?P<pk>[0-9]+)$', canalDetail),
    url(r'^recursos/$', recursos),
    url(r'^recursos/(?P<pk>[0-9]+)$', recursosDetail),
    url(r'^recursos/(?P<pk>[0-9]+)/medidas/$', medidas)
]