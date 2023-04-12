# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nome = str(input('Qual é seu nome completo? ')).strip().lower()

print(f'Seu nome tem Silva? {"silva" in nome.split()[::]}')
