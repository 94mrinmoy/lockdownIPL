from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('points/', views.points, name='points'),
    path('adminportal/', views.adminPortal, name='adminPortal'),
    path('adminportal2/', views.adminPortal2, name='adminPortal2'),

]