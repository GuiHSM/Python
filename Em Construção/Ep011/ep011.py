# -*- coding: utf-8 -*-
#Nome: Guilherme Hnerique Sampaio Marcelino


# constantes
SIM = 's'

#------------------------------------------------------------------
def main():
    '''
        (none)->none
        Função para mostrar utilização das funções busque e substitua
    '''
    nome  = input("Digite o nome de um arquivo texto: ")
    opcao = input("Digite '%s' se deseja ver o texto lido: "%(SIM))
    if opcao == SIM:
        mostre_texto = True
    else:
        mostre_texto = False
        
    # leia texto do arquivo nome
    with open(nome, 'r', encoding='utf-8') as arquivo: 
        texto = arquivo.read()

    # deseja que o texto seja exibido?    
    if mostre_texto:
        print("\nConteudo do arquivo '%s':"%(nome))
        print(texto)

    palavra      = input("Digite uma palavra a ser substituída: ")
    nova_palavra = input("Digite uma palavra substituta: ")
        
    # encontre as posições onde a palavra ocorre    
    ocorrencias = busque( palavra, texto )

    # mostre as posições encontradas
    print("\nAchei '%s' nos seguintes lugares: "%(palavra))
    print(ocorrencias)

    # crie um texto onde as ocorrências de `palavra` foram substituídas por
    # `nova_palavra`
    novo_texto = substitua( palavra, nova_palavra, texto )

    # exiba o texto criado
    print("\nNovo texto:")
    print(novo_texto)

    print("Fim dos testes.")

#------------------------------------------------------------------
#
def busque( palavra, texto ):
    ''' (str, str) -> list

    RECEBE duas strings, `palavra` e `texto`, e RETORNA uma lista
    contendo o início de cada ocorrência de `palavra` em `texto`.

    No caso de haver sobreposições de ocorrências de `palavra`, apenas
    menor índice dentre as ocorrências sobrepostas deverá ser inserido 
    na lista.

    Exemplos:
        
    In [4]: busque("mana", "ana e mariana compraram bananas")
    Out[4]: []

    In [5]: busque("bana", "ana e mariana compraram bananas")
    Out[5]: [24]

    In [6]: busque("ana", "ana e mariana compraram bananas")
    Out[6]: [0, 10, 25]

    In [7]: busque("AA", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    Out[7]: [2, 8, 10]
    '''
    i=0
    s=[]
    while i<len(texto)-len(palavra):
        j=0
        t=True
        while j<len(palavra) and t:
            if not palavra[j]==texto[i+j]:
                t=False
            j+=1
        if t:
            s+=[i]
            i+=j-1
        i+=1
    return s
    
#------------------------------------------------------------------
#
def substitua( palavra, nova_palavra, texto ):
    ''' (str, str, str) -> str

    RECEBE as strings `palavra`, `nova` e `texto` e
    RETORNA uma string onde todas as ocorrências de `palavra`
    foram substituídas pela `nova_pal`.

    No caso de haver sobreposições de ocorrências de `palavra`, apenas
    a de menor índice dentre as ocorrências sobrepostas deverá ser 
    substituída por `nova_palavra`.

    Exemplos:

    In [1]: substitua("compraram","venderem","ana e mariana compraram bananas")
    Out[1]: 'ana e mariana venderem bananas'

    In [2]: substitua("ana","ely","ana e mariana compraram bananas")
    Out[2]: 'ely e mariely compraram belynas'

    In [3]: substitua("AA", "????", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    Out[3]: 'AC????AGTC????????TTGTGTAGTGTGACGTTTT'

    In [4]: substitua("TGT", "X", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    Out[4]: 'ACAAAGTCAAAATXGTAGXGACGTTTT'
    '''
    # modifique o código abaixo para conter a sua solução.
    s= busque(palavra, texto)
    t=texto
    for i in range(len(s)):
        t= t[:s[i]-i*(len(palavra)-len(nova_palavra))] + nova_palavra + t[s[i]+len(palavra)-i*(len(palavra)-len(nova_palavra)):]
    return t


#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
