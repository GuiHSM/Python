# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import random

#####################################################################
# CONSTANTES
# Constantes definem variáveis cujos valores NÃO DEVEM ser 
# alterados durante a execução do programa. Assim você deve
# escolher bem esses valores ANTES de executar o programa.
#
# O uso de constantes é um boa prática de programação
# pois constantes ajudam a melhorar a legibilidade
# de seus programas. Por convenção, para identificar
# as constantes em um programa, vamos usar nomes com todas 
# as letras maiúsculas.
#
# As constantes abaixo são fornecidas como exemplo. Você
# pode utilizar, ou não, qualquer uma delas e ainda criar 
# outras constantes se desejar.
#
DEBUG = True       # se True, pede para digitar a semente e mostra a senha
MENOR_VALOR = 0    # menor número sorteado
MAIOR_VALOR = 10000 # limite superior para o maior número sorteado (mais 1)
MAX_TENTATIVAS = 7 # número máximos de chutes permitidos
NUM_DIGITOS  = 4   # número de dígitos da senha

#####################################################################
def main():
    '''(None) -> None 

    Coloque sua solução individual abaixo, seguindo o enunciado 
    desse exercício na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    
    '''

    print("Bem vindo ao MASTER BIME!!")
    # as linhas abaixo vão ajudar durante o desenvolvimento e depuração 
    # para deixar de executá-las, basta modificar a constante DEBUG para 
    # False. Mas lembre-se de deixá-la True antes de enviar esse EP.
    if DEBUG:
        semente = int(input("Digite o valor da semente: "))
        random.seed(semente)
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
        print("Número sorteado: ", senha)
    else:
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
        
    # escreva seu programa a seguir
    cont = 0
    certo=False
    senhaParaContagem = senha
    quantidadeDeDigitos=0
    while senhaParaContagem != 0:
        senhaParaContagem //=10
        quantidadeDeDigitos +=1
    while cont<7 and not certo:
        teste = int(input("Digite seu chute: 2"))
        numero=teste
        valor=senha
        certos=0
        while valor!=0:
            digito = numero%10
            digitoCerto= valor%10
            if digito == digitoCerto:
                certos+=1
            valor//=10
            numero//=10
        cont+=1
        print("Dígitos em posições certas do chute",cont,"/ 7 :",certos)
        if certos==quantidadeDeDigitos:
            certo = True
        
    if certo:
        print("Parabéns, você acertou!")
    else:
        print("Ha ha, você perdeu!")
    print("Fim do jogo.")

    # fim da main()

# =========================================================
# NÃO MODIFIQUE AS LINHAS ABAIXO
# ELAS SÃO NECESSÁRIAS PARA O CORRETOR AUTOMÁTICO
# =========================================================

if __name__ == "__main__":
    main()
        