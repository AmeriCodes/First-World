# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente.

name = str(input("Enter your full name: ")).strip()

name = name.split()
print('Nice to meet you!')
print(f'Your first name is {name[0]}.')
print(f'Your last name is {name[-1]}.')
