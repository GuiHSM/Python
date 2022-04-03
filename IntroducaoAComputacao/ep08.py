# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
        Aprendi a utilização da função len() na página 
        https://www.hacksparrow.com/python-length-or-size-of-list-tuple-array.html
         
        Aprendi a utilização da fução .copy() na página
        https://pt.stackoverflow.com/questions/183674/python-clonar-listas
        

'''
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import random

#####################################################################
def main():
    '''
    Essa função testa as funções pedidas para o EP08.
    Escreva outros testes que desejar.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    '''
    print("Testes do EP08")

    # testes da função tem_um_ciclo
    print("Função tem_um_ciclo()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [1,2,0,4,3]
    print(amigos1)
    print("tem_um_ciclo(%s) = %s"%(amigos1, tem_um_ciclo(amigos1)))
    print("tem_um_ciclo(%s) = %s"%(amigos2, tem_um_ciclo(amigos2)))
    # testes da função experimento
    print("Função experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)
    MINN  = int(input("Qual o número mínimo de pessoas: "))
    MAXN  = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T     = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW  = input("Você quer ver as listas com um ciclo [s/n]: ")
 
    debug = False
    if SHOW == 'S' or SHOW == 's':
        debug = True

    n = MINN
    while n <= MAXN:
        pn = experimento(n, T, debug)
        print("p(%d) = %f"%(n, pn))
        n = n + passo

###################################################################
def cria_lista_embaralhada( n ):
    ''' (int) -> list
    Retorna uma lista de tamanho n,
    contendo os números de 0 a n em ordem aleatória.
    '''
    lista = []
    i = 0
    while i < n:
        lista += [i]
        i += 1
    random.shuffle(lista)
    return lista

######################################################################
def tem_um_ciclo(amigo_de):
    ''' (list) -> bool 
    Recebe uma lista de "amigo secreto"
    e retorna True caso exista um único ciclo na lista.
    Retorna False caso contrário.
    '''
    # modifique o código abaixo para conter a sua solução.
    i=0
    j=0
    amigo_des=amigo_de.copy()
    teste=False
    final=len(amigo_des)
    while i<final-1 and (not amigo_des[j]==-1) :
        valor = amigo_des[j]
        amigo_des[j]=-1
        j=valor
        i+=1
    if not amigo_des[j]==-1:
        teste=True
    return teste

###################################################################
def experimento(N, T, debug=False):
    ''' (int, int) -> float
    Calcula a probabilidade de uma lista de "amigo secreto" com
    N participantes tenha apenas 1 ciclo. Essa probabilidade deve
    ser calculada a partir de T sorteios de listas de tamanho N, 
    e calculando a frequência relativa das listas com 1 ciclo.
    '''
    # modifique o código abaixo para conter a sua solução.

    
    i= 0
    s=0
    while i< T:
        lista=cria_lista_embaralhada(N)
        if tem_um_ciclo(lista):
            s+=1
            if(debug):
                print(s,":",lista)
        i+=1
    return s/T
 
def criarLista(n):
    ''' (int)->list
    Cria uma lista de n valores, sendo a primeira 0 e a última n-1'''
    if n==1:
        return [0]
    else:
        return [n-1]+criarLista(n-1)

#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático

if __name__ == '__main__':
    main()
