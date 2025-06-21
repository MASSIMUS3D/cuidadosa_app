from django.contrib import admin
from django.urls import path, include
from . import views  # importa a view home

urlpatterns = [
    path('', views.home, name='home'),  # página inicial
    path('admin/', admin.site.urls),
    path('paciente/', include('paciente.urls')),
    path('medicacao/', include('medicacao.urls')),
    path('alimentacao/', include('alimentacao.urls')),
    path('higiene/', include('higiene.urls')),
    path('traqueostomia/', include('traqueostomia.urls')),
    path('sinaisvitais/', include('sinaisvitais.urls')),
    path('agenda/', include('agenda.urls')),
]
