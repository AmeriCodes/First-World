# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4] # As listas no python ficam entre chaves.

escolhido = random.choice(lista)

print(f'O aluno escolhida para apagar o quadro é: {escolhido}.')

