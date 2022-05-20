from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('edit/', views.edit, name = 'edit'),
    path('edit/<int:id>/', views.edit, name = 'edit'),
    path('add/', views.add, name = 'add'),
    path('imprint/', views.imprint, name = 'imprint'),
]