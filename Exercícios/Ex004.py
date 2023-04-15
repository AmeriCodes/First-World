# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e tadas as informações possíveis sobre ele.

variável = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(variável))
print('Só tem espaços? ',variável.isspace())
print('É um número? ',variável.isnumeric())
print('É alfabético? ',variável.isalpha())
print('É alfanumérico? ',variável.isalnum())
print('Está em maiúsculas? ',variável.isupper())
print('Está em menúsculas? ',variável.islower())
print('Está captalizada? ',variável.istitle())

