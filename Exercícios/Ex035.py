# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem o não formar um triângulo.

print('=+=' * 9)
print('Analisador de triãngulos.')
print('=+=' * 9)

reta1 = float(input('Digite a primeira medida: '))
reta2 = float(input('Digite a segunda medida: '))
reta3 = float(input('Digite a terceira medida: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('As medidas digitadas formam SIM um triângulo!')
else:
    print('As medidas digitadas NÂO FORMAM um triângulo!')
