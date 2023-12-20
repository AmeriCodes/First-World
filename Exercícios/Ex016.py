# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: digite o número: 6.127, O número 6.127 tem a parte inteira de 6.

entry = float(input('Enter a real number to find its integer part: '))

print(f'The integer part of {entry} is {int(entry)}')
