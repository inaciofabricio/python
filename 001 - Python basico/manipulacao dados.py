# -*- coding: utf-8 -*-

a = 10
b = 5.5
texto = "Lorem ipsum dolor sit amet"

print('O valor de a é: ' + str(a))#necessário converter para String para poder concatenar
print('O valor de a é: %i' %a)#utilizando marcador %i para numeros inteiros

print('O valor de a é: ' + str(b))#necessário converter para String para poder concatenar
print('O valor de a é: %f' %b)#utilizando marcador %f para numeros decimais
print('O valor de a é: %.1f' %b) #Com formatação das casas após o ponto e marcador %.1f onde só haverá uma casa decimal

print('O texto da variavel texto é: ' + texto)
print('O texto da variavel texto é: %s' %texto)#utilizando marcador %s para String