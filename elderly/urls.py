from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
    path('', include('servicos.urls')),
    path('', include('perfil.urls')),
    path('', include('django.contrib.auth.urls')),
]
