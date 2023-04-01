# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Digite quantos reais você tem: '))

conv = reais / 3.27

print(f'Você poderia comprar {conv:.2f} USD.')
