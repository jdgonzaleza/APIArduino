from django.conf.urls import url, include

from .views import *

urlpatterns =[
    url('usuarios/$', crearUsuario ),
    url('canales/$', canales),
    url(r'^canales/(?P<pk>[0-9]+)$', canalDetail),

]