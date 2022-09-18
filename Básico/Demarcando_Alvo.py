# -*- coding: utf-8 -*-
#Guilherme Henrique Sampaio Marcelino

##################################################################
def main():
    '''(None) -> None

    Corpo principal da função que mapeia um alvo
    '''
    acertos = input("Digite o caractér para Acertos:")
    erros = input("Digite o carácter para Erros:")
    cont=0
    codigo = ""
    while cont<=12:
        
        y=cont
        x=-4
        while x<=6:
            if(acertou_tiro(x,y)):
                codigo+= acertos
            else:
                codigo+= erros
            x+=1
        codigo+="\n        "
        cont+=1
    print("Código:",codigo)
    # fim da main()
        
    
##################################################################
def acertou_tiro(x, y):
    '''(float ou int, float ou int) -> bool

    Essa função serve para dizer se a coordenada x,y passada está dentro ou não de um
    alvo hipotético
    '''
    # escreva o corpo de sua função acertou_tiro() a seguir
    # cuidado com a tabulação
    acertou =False
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
        acertou=True
    return acertou

if __name__ == '__main__':
    main()
