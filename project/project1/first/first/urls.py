"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.home),
    path('load_form', myapp_views.load_form),
    path('add', myapp_views.add),
    path('show', myapp_views.show),
    path('edit/<int:id>', myapp_views.edit),
    path('delete/<int:id>', myapp_views.delete),
    path('update/<int:id>', myapp_views.update),
    path('search', myapp_views.sharch),

]
