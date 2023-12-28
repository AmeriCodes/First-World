# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print("I'll think of a number between 0 and 5. Try to guess!")
pc_number = randint(0, 5)
entry = int(input('Enter a number between 0 and 5: '))

if pc_number == entry:
    print("Congratulations, you win!")
else:
    print(f"Oh, you lose!\nI was thinking of {pc_number}.")
