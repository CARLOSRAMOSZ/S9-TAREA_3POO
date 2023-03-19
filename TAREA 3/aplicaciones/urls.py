from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('datos',views.paciente, name='paciente'),
    path('datos/crear',views.crear, name='crear'),
    path('datos/editar',views.editar, name='editar'),
    path('datos/editar/<int:ID>',views.editar, name='editar'),
    path('datos/eliminar/<int:ID>',views.eliminar, name='eliminar'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
