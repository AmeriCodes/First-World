# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

def calculate_hypotenuse(opposite, adjacent):
    hypotenuse = hypot(opposite_side, adjacent_side)
    return hypotenuse


opposite_side = float(input('Enter the length of the opposite side: '))
adjacent_side = float(input('Enter the lenght of the adjacent side: '))

hypotenuse_length = calculate_hypotenuse(opposite_side, adjacent_side)

print(f'The length of the hypotenuse is: {hypotenuse_length}')
