# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceito número: '))

# Verificando quem é o menor.
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é o maior.
maior = n1
if n2 > n1 and n2 >n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior número digitado foi {maior}.')
print(f'O menor número digitado foi {menor}.')

# Do jeito que foi feito (já supondo que o n1 sejá o menor ou o maior) economiza-se algumas linhas do programa.
