# Crie um programa que leia um número inteiro e moestre na tela se ele é PAR ou IMPAR.

número = int(input('Digite um número inteiro qualquer: '))

if número % 2 == 0:
    print(f'O número {número} é PAR!')
else:
    print(f'O número {número} é IMPAR!')
