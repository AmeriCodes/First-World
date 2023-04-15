# Crie um algorítimo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

print('=' *25)
n = int(input('Digite um número inteiro: '))
print('=' *25)

d = n * 2
t = n * 3
r = n ** (1/2)

print('Analisando o número digitado percebo que:')
print(f'O dobro de {n} é {d}.\nO triplo de {n} é {t}.\nE a raiz quadrada de {n} é {r:.2f}.')
