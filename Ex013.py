# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Digite o salário do funcionário em questão R$ '))

novo_salário = salário + (salário * 0.15)

print(f'Com o reajuste de 15%, o novo salário é {novo_salário:.2f}R$.')

