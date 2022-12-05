from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from pprint import pprint

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 6

class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhes_produto.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'
    

class AdicionarAoCarrinho(View):
    def get(self,*args,**kwargs):


        http_referer = self.request.META.get('HTTP_REFERER',
        reverse('produto:lista'))

        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,"produto não existe"
            )
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao,id=variacao_id)
        variacao_estoque = variacao.estoque
        produto =  variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
           imagem =  imagem.name
        else:
            imagem =  ''

        if variacao.estoque <1:
            messages.error(
                self.request,'Sem estoque suficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao_estoque < quantidade_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no '
                    f'produto "{produto_nome}". Adicionamos {variacao_estoque}x ' 
                    f'no seu carrinho'
                ) 
                quantidade_carrinho = variacao_estoque
            
            carrinho[variacao_id]['quantidade'] = quantidade_carrinho

            carrinho[variacao_id]['preco_quantativo'] = preco_unitario * quantidade_carrinho

            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_carrinho
        else:
            carrinho[variacao_id] = {
                'produto_id ' : produto_id,
                'produto_nome' : produto_nome,
                'variacao_nome' : variacao_nome ,
                'variacao_id' : variacao_id,
                'preco_unitario' : preco_unitario,
                'preco_unitario_promocional' : preco_unitario_promocional,
                'preco_quantitativo' : preco_unitario,
                'preco_quantitativo_promocional' : preco_unitario_promocional,
                'quantidade' : 1,
                'slug' : slug,
                'imagem' : imagem,
            }

        self.request.session.save()
        pprint(carrinho)
        return HttpResponse(f'{variacao.produto}{variacao.nome}')


class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass

class Finalizar(View):
    pass