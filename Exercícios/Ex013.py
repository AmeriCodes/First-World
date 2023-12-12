# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
import os
from time import sleep
import platform

def clear_screen():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def new_salary(current, percentage):
    return f'{current + (current * percentage):.2f} Euro'

while True:
    print(f'{" Salary Adjustment of 15% ":-^40}')

    salary = str(input('Current salary: € ')).strip()

    try:
        salary = float(salary)
        break
    except ValueError:
        print('Invalid salary. Enter only numbers and decimals.')
        sleep(2)
        clear_screen()
        continue

percentage = 0.15

print(f'\nNew salary: {new_salary(salary, percentage)}')
