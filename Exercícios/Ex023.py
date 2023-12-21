# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados Ex:
# Digite o número: 1834
# unidade: 4 dezena: 3 centena: 8 milhar: 1

number = int(input('Enter a number from 0 to 9999: '))

unit = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10

print(f'Unit: {unit}')
print(f'Tens: {tens}')
print(f'Hundreds: {hundreds}')
print(f'Thousands: {thousands}')