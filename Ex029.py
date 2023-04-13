# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. Á multa vai custar R$7,00 por cada Km acima do limite.

velô = int(input('Digite a velocidade do veículo: '))

multa = 7 * (velô - 80)

if velô <= 80:
    print('Dirija com segurança e tenha um bom dia! ')
else:
    print(f'MULTADO, Você excedeu o limite de velocidade em {velô - 80}Km/h e a multa para tal infração é de {multa:.2f}R$.')
