# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

name = str(input("What's your full name? ")).strip()

print(f'Does your name contain Silva? {"silva" in name.lower()}')
