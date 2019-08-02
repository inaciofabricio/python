# -*- coding: utf-8 -*-

print(10+10)
print(10+(50+50))

print(10-10)
print(1000-80)

print(10/5)
print(10/6)

print(10*800)
print(55*5)

#Usando modulo para divis]ao

print(3%2)
print(4%2)
print(5%2)
print(7%3.1)

print(900%10 == 0)
print(900%10 != 0)

#solicitando dados ao usuario

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1 / num2
resto = num1 % num2

print(str(num1) + " divido por " + str(num2) + " é igual a: " + str(divisao))
print("O resto da divisao entre " + str(num1) + " e " + str(num2) + " é igual a: " + str(resto))

