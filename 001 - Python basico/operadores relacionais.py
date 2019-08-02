# -*- coding: utf-8 -*-

print(100==100) #verifica se é igual
print(100!=100) #verifica se é diferente
print(100>100) #verifica se é maior
print(100<100) #verifica se é menor
print(100>=100) #verifica se é maior igual
print(100<=100) #verifica se é menor igual

# OR e AND

#
if((1 > 2) or (4 > 3)):
    print('Sim')
else:
    print('Não')

#
if((1 > 2) and (4 > 3)):
    print('Sim')
else:
    print('Não')


# if elif

idade = int(input("Informe sua idade: "))

if(idade <= 0):
    print("Sua idade não pode ser menor ou igual a 0.")
elif(idade > 150):
    print("Sua idade não pode ser maior que 150 anos.")
elif(idade < 18):
    print("Você precisa ter mais de 18 anos.")
else:
    print("Sua idade é aceitavel.")