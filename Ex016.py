# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: digite o número: 6.127, O número 6.127 tem a parte inteira de 6.

número = float(input('Digite um número real: '))

parte_inteira = int(número)

print(f'A parte inteira do número {número} é {parte_inteira}.')

# Outra maneira de extrair a parte inteira de um número abaixo.

"""import math

numero_real = float(input("Digite um número real: "))  # Lê um número real

parte_inteira = math.floor(numero_real)  # Extrai a parte inteira do número

print("A parte inteira do número é:", parte_inteira)  # Mostra a parte inteira do número
"""