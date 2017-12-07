#Faça um programa que pergunte o preço de três produtos e
#informe qual produto você deve comprarsabendo que a decisão
#é sempre pelo mais barato.

nome_primeiro = input("Nome do Produto: ")
preco1 = float(input("Informe preço do primeiro produto: "))

nome_segundo = input("\nNome do Produto: ")
preco2 = float(input("Informe preço do segundo produto: "))

nome_terceiro = input("\nNome do Produto: ")
preco3 = float(input("Informe preço do terceiro produto: "))

if preco1 < preco2 and preco1 < preco3:
    print ("\nCompre o produto {} que custa {:.2f}R$".format(nome_primeiro, preco1))
elif preco2 < preco1 and preco2 < preco3:
    print ("\nCompre o produto {} que custa {:.2f}R$".format(nome_segundo, preco2))

elif preco3 < preco1 and preco3 < preco2:
    print ("\nCompre o produto {} que custa {:.2f}R$".format(nome_terceiro,preco3))
