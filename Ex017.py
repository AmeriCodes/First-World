# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hopotenusa.

import math

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)

print(f'O comprimento da hipotenusa é:{hipotenusa:.2f}')

# Outra maneira de fazer é utilizando o comando 'hypot' da biblioteca 'math', que calcula a hipotenusa.

"""from math import hypot
c_oposto = float(input('Comprimento do cateto oposto'))
c_adjacente = float(input('Comprimento do catato adjacente'))
hi = hypot(c_oposto, c_adjacente)
print(f'A hipotenusa vai medir {hi:.2f}')"""


# Outra maneira abaixo, utilizando a técnica de potenciação com expoente fracionário.

"""cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: ")) 

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5  # Calcula a hipotenusa usando a técnica de potenciação com expoente fracionário

print("O comprimento da hipotenusa é:", hipotenusa) 
"""