# -*- coding: utf-8 -*-
#Nome: Guilherme Henrique Sampaio Marcelino

'''
    Importante, um ciclo é um conjunto de valores que
    apontam para o próximo de tal maneira que retorna para
    si mesmo, [1,2,0], só possui um ciclo, enquanto [0,1,2]
    possui 3 ciclos, este programa estima a probabilidade de
    se ter apenas um ciclo para dado n
'''

import random

#####################################################################
def main():
    '''(none)->none
    Corpo de teste para a função sorteio
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
