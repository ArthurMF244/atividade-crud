from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Funcionario

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

class FuncionarioCreateView(SuccessMessageMixin, CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")
    success_message = "Funcionário cadastrado com sucesso!"

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"
    ordering = ["nome"]

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "confirmar_delete.html"
    success_url = reverse_lazy("lista_funcionarios")
