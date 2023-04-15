# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 1.250,00, calcule um aumento de 10%, para inferiores ou iguais, o aumento é de 15%.

salário = float(input('Digite o salário do funcionário: '))

aumento10 = salário + (salário * 10 / 100)
aumento15 = salário + (salário * 15 / 100)

if salário <= 1250:
    print(f'Para este salário o aumento é de 15%, indo assim para {aumento15:.2f}R$.')
else:
    print(f'Para este salário o aumento é de 10%, indo assim para {aumento10:.2f}R$.')

# Outra maneira agora sem abrir variáveis fora do 'if'
"""
salário = float(input('Digite o salário do funcionário R$: '))
if salário <= 1250:
    novo_salário = salário + (salário * 15 / 100)
else:
    novo_salário = salário + (salário * 10 / 100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo_salário:.2f}.')
"""