# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distância = int(input('Digite a distância da viagem: '))

preço_comum = 0.50
preço_desc = 0.45

if distância <= 200:
    print(f'O valor da passagem é {distância * preço_comum}R$.')
else:
    print(f'Parabéns, pela distância da viagem você recebou uma promoção, sua viagem custará {distância * preço_desc}R$.')
