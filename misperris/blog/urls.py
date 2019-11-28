from django.conf.urls import include, url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages

app_name='blog' 

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^base', views.base, name='base'),
    url(r'^Registro', views.registro, name='registro'),
    path('ajax/load-cities/', views.load_ciudades, name='load_ciudades'),
    url(r'^mascota/new/$', views.mascota_new, name='mascota_new'),
    url(r'^Mascota_List',views.mascota_list,name='mascota_list'),
    url(r'^mascota/(?P<pk>[0-9]+)/$', views.mascota_detail, name='mascota_detail'),
    url(r'^mascota/(?P<pk>[0-9]+)/edit/$', views.mascota_edit, name='mascota_edit'),
    url(r'^mascota/(?P<pk>[0-9]+)/delete/$', views.mascota_delete, name='mascota_delete'),

]

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)