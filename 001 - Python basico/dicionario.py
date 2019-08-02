# -*- coding: utf-8 -*-

dicionario = dict()

dicionario['nome'] = 'jose'
dicionario['cpf'] = '123.456.789-00'
dicionario['fone'] = '(83) 99999-9999'

print(dicionario)
print('')
print('Seu nome é: ' + dicionario['nome'])
print('Seu cpf é: ' + dicionario['cpf'])
print('Seu telefone é: ' + dicionario['fone'])

print('')

#função popitem
print(dicionario)
dicionario.popitem()
print(dicionario)
dicionario.popitem()
print(dicionario)
dicionario.popitem()
print(dicionario)

dicionario['nome'] = 'Jose Maria'
dicionario['cpf'] = '123.456.789-00'
dicionario['fone'] = '(83) 99999-9999'
print(dicionario)

print('')

