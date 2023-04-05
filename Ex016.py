# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: digite o número: 6.127, O número 6.127 tem a parte inteira de 6.

número = float(input('Digite um número real: '))

parte_inteira = int(número)

print(f'A parte inteira do número {número} é {parte_inteira}.')


# Também da pra fazer utilizando a função 'trunc' da biblioteca 'math', que corta a parte flutuante do número.

"""from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitedo foi {num} e a sua porção inteira é {trunc(num)}.')"""


# Outra maneira de extrair a parte inteira de um número é utilizando a função de arredondamento para baixo 'floor'.

"""import math

numero_real = float(input("Digite um número real: "))

parte_inteira = math.floor(numero_real)

print("A parte inteira do número é:", parte_inteira)"""