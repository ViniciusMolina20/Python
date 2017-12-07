#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd'

nome = input("Digite seu nome: ")

while len(nome) <= 3:
    print ("\nNome Invalido")
    nome = input("Digite seu nome: ")

idade = int(input("\nDigite sua idade: "))

while idade < 0 or idade > 150:
    print ("\nIdade invalida")
    idade = int(input("Digite sua idade: "))

salario = float(input("\nDigite seu salario: "))

while salario <= 0 :
    print ("\nSalario Invalido")
    salario = float(input("Digite seu salario: "))

sexo = input("\nDigite seu Sexo [M/F]: ")

while sexo != "m" and sexo != "M" and sexo != "f" and sexo != "F":
    print ("\nSexo Invalido")
    sexo = input("Digite seu Sexo [M/F]: ")

est_civil = input("\nDigite seu Estado Civil [S-Solteiro/C-Casado/V-Viuvo/D-Divorciado]: ")

while est_civil != "s" and est_civil != "S" and est_civil != "c" and est_civil != "C" and est_civil != "v" and est_civil != "V" and est_civil != "d" and est_civil != "D":
    print ("\nEstado Civil invalido")
    est_civil = input("Digite seu Estado Civil [S-Solteiro/C-Casado/V-Viuvo/D-Divorciado]: ")

print ("\nNome: {}".format(nome))
print ("Idade: {} anos".format(idade))
print ("Salario: {:.2f}R$".format(salario))

if sexo == "m" or sexo == "M":
    print ("Sexo: Masculino")

else:
    print ("Sexo: Feminino")

if est_civil == "s" or est_civil == "S":
    print ("Estado Civil: Solteiro(a)")

elif est_civil == "c" or est_civil == "C":
    print ("Estado Civil: Casado(a)")

elif est_civil == "v" or est_civil == "V":
    print ("Estado Civil: Viuvo(a)")

else:
    print ("Estado Civil: Divorciado(a)")









    








