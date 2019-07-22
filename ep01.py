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
        
        Eu retirei a função print() da pagina http://wiki.qpython.org/doc/program_guide/
'''

def main():
    '''(None) -> None 

    Coloque sua solução individual abaixo, seguindo o enunciado do 
    exercício EP01 na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515

    SUGESTÃO: Simule o programa antes de executar 
    cada exemplo. Em particular, para cada expressão, 
    além do valor do resultado, você deve saber se o 
    tipo do resultado é int, float ou str.

    '''
    # escreva seu programa a seguir
    p = input("Digite uma palavra p: ")
    i = int(input("Digite um inteiro i: "))
    r = float(input("Digite um real r: "))
    print("")
    print("Resultado de p + p: "+(p+p))
    print("Resultado de i + i: "+str(i+i))
    print("Resultado de r + r: "+str(r+r))
    print("Resultado de i * p: "+(i*p))
    print("Resultado de i * i: "+str(i*i))
    print("Resultado de i * r: "+str(i*r))
    print("Resultado de r / i: "+str(r/i))
    print("Resultado de 2 * i / i: "+str(2*i/i))
    print("Resultado de i / i * 2: "+str(i/i*2))

    # fim da main()

# =========================================================
# NÃO MODIFIQUE AS LINHAS ABAIXO
# ELAS SÃO NECESSÁRIAS PARA O CORRETOR AUTOMÁTICO
# =========================================================

if __name__ == "__main__":
    main()

