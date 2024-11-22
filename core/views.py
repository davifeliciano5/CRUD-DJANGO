from django.urls import reverse_lazy

from .models import Professor
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class ListaProfessor(ListView):
    model = Professor
    template_name = 'professor.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CriaProfessor(CreateView):
    model = Professor
    fields = ['nome','cref']
    template_name ='criandoprofessor.html'
    success_url = reverse_lazy('professor')

class EditandoProfessor(UpdateView):
    model = Professor
    template_name = 'edita.html'
    fields = ['nome','cref']
    success_url = reverse_lazy('professor')

class Removeprofessor(DeleteView):
    model = Professor
    success_url = reverse_lazy("professor")
    template_name = 'deleta.html'
    fields = ['nome','cref']

