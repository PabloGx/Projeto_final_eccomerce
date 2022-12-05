from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class Pagar(View):
    def get(self,*args, **kwargs):
        return HttpResponse('pagar')

class FecharPedido(View):
    def get(self,*args, **kwargs):
        return HttpResponse('FecharPedido')

class Detalhe(View):
    def get(self,*args, **kwargs):
        return HttpResponse('Detalhe')

