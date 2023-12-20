# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

def calculate_trigonometric_values(angle):

    angle_radians = math.radians(angle)

    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)

    print(f'Sine of {angle} degrees: {sine_value}')
    print(f'Cosine of {angle} degrees: {cosine_value}')

    if angle % 180 != 90:
        print(f'Tangent of {angle} degrees: {tangent_value}')
    else:
        print(f'Tangent of {angle} degrees is undefined.')


angle_input = float(input('Enter an angle in degrees: '))

calculate_trigonometric_values(angle_input)
