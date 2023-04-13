# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

aleatório = random.randint(0, 5)

print('-=-' * 20)
print('Tente adivinhar o número de 0 a 5 que estou pensando. . . ')
print('-=-' * 20)

tentativa = int(input('Em que número eu pensei? '))
print('PROCESSANDO. . .')
sleep(2)

if tentativa == aleatório:
    print(f'Eu tinha pensado exatamente em {tentativa}, Parabêns seu sortudo!')
else:
    print(f'Eu pensei em {aleatório}, não foi dessa vez.')
    