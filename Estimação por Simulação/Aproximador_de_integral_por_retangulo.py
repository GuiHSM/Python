
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome: Guilherme Henrique Sampaio Marcelino
    NUSP: 11222061

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

#------------------------------------------------------------------
# Constantes que você pode utilizar nesse exercício

EPSILON  = 1.0e-6
MAIOR=1e6
#------------------------------------------------------------------
# O import abaixo carrega algumas funções do módulo math,
# associando elas a outros nomes. Assim, vc pode usar a função
# math.exp como FUNCAO_EXP, math.sin como FUNCAO_SIN, etc.

import math

#------------------------------------------------------------------

def main():
    '''
    (None) -> None
    Main função para testar e exemplificar as funções de aproximação de integral.
    '''
    # modifique a atribuição para a funcao_x que desejar como:
    # funcao_x = math.cos # ou 
    # funcao_x = math.sin # ou
    # funcao_x = math.exp # etc, para integração com outras funções.
    funcao_x = funcao_2     # a funcao_1, funcao_2, e funcao_3
                            # estão definidas mais abaixo.
    nome = funcao_x.__name__ # pega o nome da funcao_x usada!?

    # Testes da funcao_x
    print("funcao_x usada nesses testes: ", nome)
    print("Valor de funcao_x em 0.0: ", funcao_x( 0.0 ))
    print("Valor de funcao_x em 0.5: ", funcao_x( 0.5 ))
    print("Valor de funcao_x em 1.0: ", funcao_x( 1.0 ))

    # testes da função integral_por_retangulos
    print()
    print("Integral por retângulos:")
    a=1e-6
    b=1
    k = 1
    n = 3
    while n > 0:    
        print("para %d retangulos no intervalo [%f, %f]:"%(k, a, b))
        print("---> integral: ", integral_por_retangulos(funcao_x,a,b,k))
        k *= 10
        n -= 1

    # testes da função aproxima_integral
    print()
    print("Aproxima Integral:")
    a = 1e-6
    b = 1
    area, k = aproxima_integral(funcao_x, a, b)
    print("para eps = %f e intervalo [%f, %f]:"%(EPSILON, a, b))
    print("---> integral = %f, com %d retângulos."%(area, k ))
    eps = 1e-6

    n = 3
    while n > 0: 
        eps *= 10
        area, k = aproxima_integral(funcao_x, a, b, eps)
        print("para eps = %f e intervalo [%f, %f]:"%(eps, a, b))
        print("---> integral = %f, com %d retângulos."%(area, k ))
        n -= 1
 
    print("Fim dos testes.")
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função linear
def funcao_1 ( x ):
    ''' (float) -> float 
    função auxiliar x
    '''
    return x
#------------------------------------------------------------------
def funcao_2 ( x ):
    ''' (float) -> float 
    Função auxiliar sqrt(1 - x*x)
    '''
    y = math.sqrt( 1 - x*x )    
    return y
#------------------------------------------------------------------
def funcao_3 ( x ):
    ''' (float) -> float 
    função auxiliar e^x
    '''
    y = math.exp( x )
    return y
#------------------------------------------------------------------
#
def erro_rel(y, x):
    ''' (float, float) -> float
    Recebe dois números reais x e y e retorna o erro relativo entre eles.
    Exemplo:
    >>> erro_rel(0, 0)
    0.0
    >>> erro_rel(0.01, 0)
    1.0
    >>> erro_rel(1.01, 1.0)
    0.01
    '''
    if x == 0.0 and y == 0.0:
        return 0.0
    
    if y == 0:
        return 1.0
    
    erro = (y-x)/x
    if erro < 0:
        return -erro
    return erro
#------------------------------------------------------------------
#
def integral_por_retangulos(f, a, b, k):
    '''(função, float, float, int) -> float
    Calcula uma aproximação da integral da função f
    no intervalo [a,b] usando k retângulos.
    '''
    # escreva a sua solução a seguir
    # remova ou modifique a linha abaixo como desejar
    area = 0.0;
    i=0
    while i<k:
        area += f(((a + i*((b-a)/k)) +((i+1)*((b-a)/k)))/2)
        i +=1
    
    return ((b-a)/k)*area
#------------------------------------------------------------------
#
def aproxima_integral(f, a, b, eps=EPSILON):
    '''(função, float, float, float) -> float, int
    Calcula uma aproximação da integral da função f 
    no intervalo [a,b] usando o número de retângulos 
    suficiente para que o erro relativo seja menor que eps. 
    Para melhorar o desempenho dessa função, os valores de k devem 
    dobrar a cada iteração. Ou seja, k assume valores na sequência 
    1, 2, 4, 8, 16, etc.
    A função retorna 2 valores, o valor da aproximação e o valor 
    de k usado para atingir essa aproximação.
    A função possui dois problemas, o primeiro é caso a seja igual a 0
    o erro relativo não funcionará e irá loopar infinitamente, esse é o
    dilema do erro relativo, e o segundo é que aproximar a integral por
    retangulos nunca foi o mais efetivo, então para certos valores de eps,
    k será tão grande que não irá rodar em menos de 10 min, então por isso 
    limitei superiormente k
    '''
    # escreva o corpo da função
    k=1
    x=a+(b-a)/k
    erro_relativo_um=False
    while eps< erro_rel(a, x):
        k*=2
        x=a+(b-a)/k
        if (not erro_relativo_um) and erro_rel(a, x)==1.0:
            erro_relativo_um=True
        elif erro_relativo_um and erro_rel(a, x)==1.0:
            print("Erro, zero da função está no intervalo")
            break
    if(k>MAIOR):
        print("Não é possível para esse eps")
        k=MAIOR
    teste = integral_por_retangulos(f,a,b,k);
    # remova ou modifique a linha abaixo como desejar
    return teste, k  # para retornar um float e um int, 
                   # basta separá-los por vírgula :-)

#######################################################
###                 FIM                             ###
#######################################################
# 
#  Não modifique as linhas abaixo
# 
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático         

if __name__ == '__main__':
    main()
