# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias de aluguel: '))
km = int(input('Quantos quilômetro percorridos: '))

diária = dias * 60
quilometragem = km * 0.15
total_a_pagar = diária + quilometragem

print(f'Analisando as informações fornecidas o valor fica por {total_a_pagar:.2f}R$')
