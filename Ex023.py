# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados Ex:
# Digite o número: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

import time

número = int(input('Digite um número inteiro de 0 a 9999 para analise: '))

u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10

print('Analisando. . .')
time.sleep(2)

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
