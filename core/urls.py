"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,),
    path('mahsulotlar/',mahsulot_view,name='mahsulotlar'),
    path('mahsulotlar/<int:mahsulot_id>/',mahsulot_index_view),
    path('mahsulotlar/<int:mahsulot_id>/delete/',mahsulot_delete),
    path('mahsulotlar/<int:mahsulot_id>/update/', mahsulot_update),
    path('mijozlar/',mijoz_view,name='mijozlar'),
    path('mijozlar/<int:mijoz_id>',mijoz_index_view),
    path('mijozlar/<int:mijoz_id>/delete/', mijoz_delete),
    path('buyurtmalar/',buyurtma_view,name='buyurtmalar'),
    path('buyurtmalar/<int:buyurtma_id>',buyurtma_index_view),
    path('buyurtmalar/<int:buyurtma_id>/delete',buyurtma_delete),
]