# -*- coding: utf-8 -*-

lista = [1,2,3,4,5]

print(lista)#todos os elementos
print(lista[0])#primeiro elemento
print(lista[-1])#ultimo elemento

print('')
print('')

#imprimindo a lista com for
for x in lista:
    print(x)

#lista de listas

nova_lista = [[1,2,3],['a','b','c']]
print(nova_lista)
print(nova_lista[0])
print(nova_lista[1])

print('')
print('')

#imprimido a lista que ta dentro da lista
for a in nova_lista:
    for y in a:
        print(y)



numero = [1,2,3,4,5]
print(numero)

#incluindo um elemnto na lista
numero.append(6)
print(numero)

#excluindo um elemnto na lista
del(numero[-1])
print(numero)
