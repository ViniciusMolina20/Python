# Python
Codigos de Python
#Faça um Programa que peça um valor
#e mostre na tela se o valor é positivo ou negativo.

#Vinicius Molina

n1 = int(input("Digite um valor: "))

if n1 > 0:
    print ("O numero {} é Positivo".format(n1))

elif n1 == 0:
    print ("O numero 0 não é nem Positivo nem Negativo")
    
else:
    print ("O numero {} é Negativo".format (n1))
