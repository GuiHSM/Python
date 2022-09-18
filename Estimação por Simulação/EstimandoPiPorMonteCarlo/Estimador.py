#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
#Escreva seu nome e numero USP
INFO = {12345678:"Fulano Junior"}
def estima_pi(Seed = None):

    random.seed(Seed)
    #random.random() gera um numero com distribuicao uniforme em (0,1)
    """
    Esta funcao deve retornar a sua estimativa para o valor de PI
    Escreva o seu codigo nas proximas linhas
    """
    """
    Inicializando a soma dos valores de T(x) e definindo n
    """
    n=49000000
    soma=0
    """
    Iniciando o looping que simboliza o somátorio na fórmula da proporção
    """
    
    for i in range(n):
         """
         Gerando x1 e x2, sendo x=[x1,x2], de forma uniformemente variado 
         """
         x1 = random.uniform(-1,1)
         x2 = random.uniform(-1,1)
         if x1*x1+x2*x2<=1:
              soma+=1
    """
    Por fim, defindo pi como 4 vezes a proporcao entre pontos que pertencem ao círculo e pontos que 
    pertencem ao quadrado     
    """
    pi=4*soma/n
    
    return pi
