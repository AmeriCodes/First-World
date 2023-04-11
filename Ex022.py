# Crie um programa que leia o nome completo de uma pessoa e mostre.
# 1. O nome com todas as letras maiúsculas
# 2. O nome com todas as letras menúsculas
# 3. Quantas letras ao todo (sem considerar espaços)
# 4. Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()

print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}.')
print(f'Seu nome com todas as letras menúsculas: {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.') # Por algum motivo usando o f-string, foi necessário utilizar aspas duplas dentro dos parenteses, coisas que não seria necessária utilizando o .format.
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')

# *Outra maneira de fazer.*

"""
nome_completo = input("Digite seu nome completo: ")

nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()

total_letras = len(nome_completo.replace(" ", ""))

primeiro_nome = nome_completo.split()[0]
total_letras_primeiro_nome = len(primeiro_nome)

print(f"Nome em letras maiúsculas: {nome_maiusculo}")
print(f"Nome em letras minúsculas: {nome_minusculo}")
print(f"Total de letras (sem considerar espaços): {total_letras}")
print(f"Total de letras no primeiro nome: {total_letras_primeiro_nome}")
"""