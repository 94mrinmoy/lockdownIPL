from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('points/', views.points, name='points'),
    path('adminportal/', views.adminPortal, name='adminPortal'),
    path('adminportal2/', views.adminPortal2, name='adminPortal2'),
    path(
        'sw.js',
        TemplateView.as_view(template_name='sw.js', content_type='application/javascript'),
        name='sw.js',
    ),

    # path('static/a', views.index, name='index'),

]