# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

import os
from time import sleep
import platform

def clear_screen():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def wall_area(width, height):
    return width * height


def paint_quantity_needed(wall_area):
    return wall_area / 2


while True:
    print(f'{"Painting App":=^44}')
    print(f'{"Find out how much paint you need!":^44}\n')
    wall_width = str(input('Wall width: '))
    wall_height = str(input('Wall height: '))

    try:
        wall_width = float(wall_width)
        wall_height = float(wall_height)
        break
    except ValueError:
        print("Invalid value. Please try again.")
        sleep(2)
        clear_screen()
        continue


wall_area_value = wall_area(wall_width, wall_height)
paint_quantity_needed_value = paint_quantity_needed(wall_area_value)

print(f'\nThe wall area is {wall_area_value:.2f}m²')
print(f'The quantity of paint needed is {paint_quantity_needed_value:.2f} liters')
