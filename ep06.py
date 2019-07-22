# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''
    Nome: Guilherme Henrique Sampaio Marcelino
    NUSP:11222061

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

##################################################################
def main():
    '''(None) -> None

    Coloque sua solução individual abaixo, seguindo o enunciado do
    exercício disponível na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    '''
    # escreva o corpo da função main() a seguir
    # cuidado com a tabulação
    n= int(input("Digite N:"))
    a = int(input("Digite dígito para A:"))
    e = int(input("Digite dígito para E:"))
    cont=0
    codigo = ""
    while cont<=12:
        
        y=cont
        x=-4
        while x<=6:
            if(acertou_tiro(x,y)):
                codigo+= str(a)
                print("    Acertou")
            else:
                codigo+= str(e)
                print("    Errou")
            x+=1
        cont+=1
    print("Código:",codigo)
        
    
##################################################################
def acertou_tiro(x, y):
    '''(float ou int, float ou int) -> bool

    Essa função serve para dizer se a coordenada x,y passada está dentro ou não do alvo
    passado no texto do ep6 de MAC0110 do 1ºsemestre de 2019 disponivel no site 
    paca.ime.usp.br na aba do curso
    '''
    # escreva o corpo de sua função acertou_tiro() a seguir
    # cuidado com a tabulação
    queijo =False
    fileira1=((y<=12 and y>=11)or((y<11 and y>=10.5)and(not -1<x<1))or((y<10.5 and y>10)and(not (-0.5>x>-1 or 0.5<x<1))))and(x<6 and x>=-4)
    fileira2=(((y<=10 and y>=9.5) and (not(-1<x<-0.5 or 1>x>0.5)))or(9>y>8))and(-2<x<2)
    quadrado1 = ((-3<=x and x<-2)and(4<=y and y<5))
    quadrado2 = ((4<x and x<=5)and(6<=y and y<7))
    quadrado3 = (2<x and x<=3)and(4<=y and y<5)
    quadrado4 = ((-1<=x and x<=1)and(2<y and y<=3))or(x==1 and y==2)or(x==-1 and y==2)
    formaMaior1 = ((((x-y<0) and x-y>=-4)and(x<=4 and x>=0))or((x-y<0 and y<=8)and(x<6 and x>4)))
    formaMaior2 = ((-x-y<0) and -x-y>=-4)and(x>=-4 and x<0)
    quina = (x==-2 and y==4)or(x==-3 and y==5)or(x==2 and y==4)or(x==3 and y==5)or(x==4 and y==6)or(x==5 and y==7)
    if (fileira1 or fileira2 or formaMaior2 or formaMaior1)and(not(quadrado1 or quadrado2 or quadrado3 or quadrado4 or quina)):
        queijo=True
    return queijo
#######################################################
###                 FIM   DA   MAIN()               ###
#######################################################
#
#  Não modifique as linhas abaixo
#
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático

if __name__ == '__main__':
    main()