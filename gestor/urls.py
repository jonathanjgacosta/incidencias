from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from incidencias.views import IncidenciaListView, IncidenciaView, IncidenciaUpdateView, IncidenciaCreateView
from incidencias.views import EscalarCreateView, EscalarListView
from incidencias.views import ComentarioListView, ComentarioUpdateView, ComentarioCreateView

admin.autodiscover()
urlpatterns = patterns('',
url(r'^$','usuarios.views.inicio'),
url(r'^iniciar_sesion/','usuarios.views.inicio_sesion'),
url(r'^cierre_sesion/','usuarios.views.cierre_sesion'),
url(r'^sesion_fallida/','usuarios.views.inicio'),
url(r'^incidencia/nuevo/$', IncidenciaCreateView.as_view(), name='incidencia_nuevo'),
url(r'^incidencia/listado/$', IncidenciaListView.as_view(), name='incidencia_listado'),
url(r'^incidencia/detalle/(?P<pk>\d+)/$', IncidenciaView.as_view(), name='incidencia_detalle'),
url(r'^incidencia/editar/(?P<pk>\d+)/$', IncidenciaUpdateView.as_view(), name='incidencia_editar'),
url(r'^escalada/nuevo/(?P<id>\d+)/$', EscalarCreateView.as_view(), name='escalada_nuevo'),
url(r'^escalada/listado/$', EscalarListView.as_view(), name='escalada_listado'),
url(r'^comentario/nuevo/(?P<id>\d+)/$', ComentarioCreateView.as_view(), name='comentario_nuevo'),
url(r'^comentario/listado/(?P<id>\d+)/$', ComentarioListView.as_view(), name='comentario_listado'),
url(r'^comentario/editar/(?P<pk>\d+)/$', ComentarioUpdateView.as_view(), name='comentario_editar'),
url(r'^panel_principal/','incidencias.views.ir_panel'),
url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
url(r'^admin/', include(admin.site.urls)),
url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)