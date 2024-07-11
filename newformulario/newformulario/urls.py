"""newformulario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLcon f
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Views.HomeView import HomeView
from newformulario.Models.reclamo import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('pagina/', HomeView.pagina1, name='pagina1'),
    path('pagina2/<int:parametro1>', HomeView.pagina2, name='pagina2'),
    path('formulario/',  views.registroReclamo, name='formulario'),



]
