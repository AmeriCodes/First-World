# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

def print_multiplication_table(number):
    print(f'\n----- Multiplication Table for {number} -----\n')
    for i in range(1, 11):
        print(f'{number} x {i:>2} = {number * i}')

print('----- Multiplication Table App -----\n')

while True:
    entry = str(input('Enter a number: '))
    try:
        entry = int(entry)
    except ValueError:
        print('Invalid entry, please enter an integer!')
        continue

    print_multiplication_table(entry)

    choice = input('\nDo you want to see the multiplication table for another number? (yes/no): ').lower()
    if choice != 'yes':
        print('Exiting the app. Goodbye!')
        break
