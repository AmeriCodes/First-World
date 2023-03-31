# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e minímetros

print('==' *15)
metro = int(input('Digite uma valor em metros: '))
print('==' *15)

cen = metro * 100

mil = metro * 1000

print(f'Convertendo para centímetros resulta em {cen}.\nE convertendo para milímetros temos {mil}.')
