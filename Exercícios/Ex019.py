# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

import os
from time import sleep
import platform
import random

def the_cleaner(lst, key_cleaner):
    print(f'And the winner is.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.\n')
    sleep(1)
    print(f"!!{lst[key_cleaner]:^18}!!")

def clear_screen():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

students = {
    'male': {
        1: 'Matthew',
        2: 'George',
        3: 'Josh',
        4: 'Allen',
        5: 'Oscar',
    },
    'female': {
        1: 'Emily',
        2: 'Taylor',
        3: 'Eleonor',
        4: 'Britney',
        5: 'Elie',
    },
}

while True:
    print(f'{" Find out the board cleaner ":-^40}')

    try:
        sex_choice = str(input('[m]ale\n[f]emale\n:'))
        if sex_choice != 'm' and sex_choice != 'f':
            print('Entry invalid, please choose "m" or "f"!')
            sleep(2)
            clear_screen()
            continue
        else:
            if sex_choice == 'm':
                random_male_key = random.randint(1, len(students['male']))
                the_cleaner(students['male'], random_male_key)
            else:
                random_female_key = random.randint(1, len(students['female']))
                the_cleaner(students['female'], random_female_key)
            break
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        print('Please try again.')







"""
import random

student1 = str(input('First student: '))
student2 = str(input('Second student: '))
student3 = str(input('Third student: '))
student4 = str(input('Fourth student: '))

students = [student1, student2, student3, student4]

chosen_student = random.choice(students)

print(f'The chosen student to erase the board is: {chosen_student}')
"""