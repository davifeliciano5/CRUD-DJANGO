from tkinter.font import names

from django.urls import path,include
from core.views import ListaProfessor,CriaProfessor,EditandoProfessor,Removeprofessor


urlpatterns = [
    path('',ListaProfessor.as_view(),name='professor'),
    path('cria/',CriaProfessor.as_view(),name='criaprofessor'),
    path('<int:pk>/edita/',EditandoProfessor.as_view(),name='editandoprofessor'),
    path('<int:pk>/remove/',Removeprofessor.as_view(),name='removeprofessor'),
]