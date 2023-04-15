# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o valor do produto R$: '))

desc = preço * 0.05
novo_preço = preço - desc

print(f'Parabéns, você recebeu um desconto de 5%, seu produto agora custa {novo_preço:.2f}R$.')
