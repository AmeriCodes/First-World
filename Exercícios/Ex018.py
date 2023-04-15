# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo em graus: ')) # Uma informação importante é que os parâmetros de Seno, Cosseno e Tangente estão em Radianos e não em graus, então é necessário converter primeiro.

angulo_em_radianos = math.radians(angulo)

seno = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)

print(f'O SENO de {angulo} graus é {seno:.2f}')
print(f'O COSSENO de {angulo} graus é {cosseno:.2f}')
print(f'A TANGENTE de {angulo} graus é {tangente:.2f}')

