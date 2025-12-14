from django.urls import path
from .views import (
    FuncionarioCreateView,
    FuncionarioListView,
    FuncionarioUpdateView,
    FuncionarioDeleteView
)

urlpatterns = [
    path("form_funcionario", FuncionarioCreateView.as_view(), name="form_funcionario"),
    path("lista_funcionarios", FuncionarioListView.as_view(), name="lista_funcionarios"),
    path("editar/<int:pk>", FuncionarioUpdateView.as_view(), name="editar_funcionario"),
    path("deletar/<int:pk>", FuncionarioDeleteView.as_view(), name="deletar_funcionario"),
]
