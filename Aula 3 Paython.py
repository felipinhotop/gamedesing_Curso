idade = 4

if idade == 1:
    print('A criança tem 1 ano')
elif idade == 2:
    print('A criança tem 2 anos')
elif idade == 3 :
    print('A crinaça tem 3 anos')
else: 
    print('A criança tem mais de 3 anos')
#-----------------------------------------------------------------------
opcao = 'S'
while opcao == 'S' :
   nome = input("Insira seu nome: ")
   rm = int(input("Insira seu Rm: "))
   media = int(input("Digite a media necessaria: "))
   print(nome," Rm:", rm)
    
   prova1 = int(input("Prova 1: "))
   prova2 = int(input("Prova 2: "))
   prova3 = int(input("Prova 3: "))
   prova4 = int(input("Prova 4: "))
 
   res = (prova1+ prova2 + prova3 + prova4) / 4

   if res >= media : 
     print(res, "Aprovado")
   else:
    print(res, "Reprovado")
   opcao = input("Deseja continuar? S= sim e N= nao: ")

#-----------------------------------------------------------------------
n=0
contador=0
while n<=3 :
   print("Felipe", contador)
   contador = contador +1
   n = n +1