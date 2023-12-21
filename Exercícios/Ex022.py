# Crie um programa que leia o nome completo de uma pessoa e mostre.
# 1. O nome com todas as letras maiúsculas
# 2. O nome com todas as letras menúsculas
# 3. Quantas letras ao todo (sem considerar espaços)
# 4. Quantas letras tem o primeiro nome.

full_name = str(input('Enter your full name: ')).strip()

print(full_name.upper())
print(full_name.lower())

splited_name = full_name.split()
concatenated_name = ''.join(splited_name)

print(f'At all, we have {len(concatenated_name)} letters in {full_name}.')

# A simpler way to do this.
# print(f'At all, we have {len(full_name) - full_name.count(" ")} letters in {full_name}.')

print(f'Your first name {full_name[:full_name.find(" ")]} has {full_name.find(" ")} letters.')
