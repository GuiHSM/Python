# -*- coding: utf-8 -*-
#Guilherme Henrique Sampaio Marcelino

import random

DEBUG = True       # se True, pede para digitar a semente e mostra a senha
MENOR_VALOR = 0    # menor número sorteado
MAIOR_VALOR = 1000 # limite superior para o maior número sorteado (mais 1)
MAX_TENTATIVAS = 5 # número máximos de chutes permitidos

#####################################################################
def main():
    '''(None) -> None 

    Função principal responsável por todo o jogo
    de adivinhar senhas
    
    '''

    print("Bem vindo ao MASTER BIME!!")
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

if __name__ == "__main__":
    main()
        
