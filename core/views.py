from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto


class IndexView(ListView):  # Classe que herda de ListView
    models = Produto  # models recebendo Produto criado no Models da aplicaçao
    template_name = 'index.html'  # Nome do template sendo utilizado
    queryset = Produto.objects.all()  # Esta retornando todos os objetos (Produto) armazenados no queryset = bd
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'  # Utilizando o formulário(layout) criado no template
    fields = ['nome', 'preco']  # Campos selecionados
    success_url = reverse_lazy('index')  # Em havendo sucesso no cadastro redirecionar para (index)


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'  # Nesse caso precisamos criar um template
    success_url = reverse_lazy('index')
