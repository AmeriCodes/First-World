# Crie um programa que leia um número inteiro e moestre na tela se ele é PAR ou IMPAR.

number = int(input('Enter a integer number: '))

if number % 2 == 0:
    print(f'{number} is a EVEN number!')
else:
    print(f'{number} is a ODD number!')

