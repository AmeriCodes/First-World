# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. ps: fiz este exercicio utilizando a cotação do dia. . .

import time

real = float(input('Quantos reais você tem na sua carteira? R$:'))
print('-' * 15)

lira_turca = real / 0.27129
peso_argentino = real / 0.024
peso_chileno = real / 0.00646
peso_colombiano = real / 0.0011
iene_japones = real / 0.03923
dolar = real / 5.20
euro = real / 5.58
franco_suico = real / 5.61
libra_esterlina = real / 6.26
dinar_kuwaitiano = real / 17.00

print(f'Analisando as cotações do dia. . .: ')
print('-' * 15)

time.sleep(2)

print('Aguarde alguns segundos. . .')
print('-' * 15)

time.sleep(5)

print(f'COP:{peso_colombiano:.2f} Pesos Colombianos.')
print(f'ARS:{peso_argentino:.2f} Pesos Argentinos.')
print(f'CLP:{peso_chileno:.2f} Pesos Chilenos.')
print(f'JPY:{iene_japones:.2f} Ienes Japoneses.')
print(f'TRY:{lira_turca:.2f} Liras Turcas.')
print(f'USD:{dolar:.2f} Dólares.')
print(f'EUR:{euro:.2f} Euros.')
print(f'CHF:{franco_suico:.2f} Francos Suíços.')
print(f'GBP:{libra_esterlina:.2f} Libras Esterlinas.')
print(f'KWD:{dinar_kuwaitiano:.2f} Dinares Kuwaitianos.')
# TRY, ARS, CLP, COP, JPY, USD, EUR, CHF, GBP, KWD.