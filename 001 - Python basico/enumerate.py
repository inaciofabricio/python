# -*- coding: utf-8 -*-

lista = ['a','b','c','d','e']
print(lista)

print('')

nova_lista = enumerate(lista)

for x in nova_lista:
    print(x)

print('')

#metodo reverse

lista.reverse()
print(lista)

#ordenando na ordem alfabetica
lista.sort()
print(lista)


print('')

#descobrindo a quantidade de elementos da lista
print(len(lista))