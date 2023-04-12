# Faça um programa que leia um frase pele teclado e mostre :
# 1 - Quantas vezes aparece a letra "A"
# 2 - Em que posição ela aparece pela primeira vez.
# 3 - Em que posição ela aparece pela última vez.

import time

frase = str(input('Digite uma frase ou um texto: ')).strip().upper()
print('. . .')
time.sleep(1)
print('Analisando frase, aguarde. . .')
time.sleep(3)

print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A aparece na posição {frase.find("A")}.')
print(f'A última letra A aparece na posição {frase.rfind("A")}.')
