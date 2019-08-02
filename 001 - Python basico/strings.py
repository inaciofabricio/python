# -*- coding: utf-8 -*-

frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
print(frase)

print('')

#função replace
frase = frase.replace('o','O')
print(frase)

print('')

#função split
frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
frase = frase.split(',')
print(frase)

#concatenando string
nova_string = frase[0] + ', ' + frase[1]
print(nova_string)

print('')

#Iterando String
frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
i = 0
while i < len(frase):
    print(i,frase[i])
    i += 1