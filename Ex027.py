# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip().split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {nome[len(nome) - 1]}')

# Uma maneira mais fácil de fazer seria substituir a última linha do código por

#* print(f'Seu último nome é {nome[-1]})
