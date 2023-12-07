from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('pybot/', views.pybot, name='pybot'),
]