#repetiçao
nome = input("escreva seu nome: ")
vezes = int(input("deseja repetir quantas vezes? "))
x = 1
while x<=vezes:
    print(nome)
    x+=1
print("termino")
#------------------------------------------------------------
print()
def repete_nome(n,num):
    #nome=input("digite o nome: ")
    #vezes = int(input("repetir quantas vezes?"))
    x=1
    while x<=num:
        print(n)
        #x=x+1
        x+=1
nome=input("digite o nome: ")
vezes = int(input("repetir quantas vezes? "))
repete_nome(nome,vezes)
print("fim")
print("")
print("------------------")
repete_nome("Mara da Silva", 3)    
#------------------------------------------------------------
print("")
# jogo de adivinhar
from random import randint
print("Bem vindo!")
print("digite um numero 1 a 100!")
sorteado = randint(1, 100)
chute = 0
while chute != sorteado:
    chute = int(input('Chute: '))
    if chute > sorteado:
        print("alto")
    else:
        print("Baixo")
print("Fim de jogo!")
