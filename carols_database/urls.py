from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home),
    path('test',views.test),
    path('finalcount/', views.finalcount, name = 'finalcount'),
    path('troll/', views.troll),


]
