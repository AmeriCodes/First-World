# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input(f'Digite a altura da parede: '))
largura = float(input(f'Digite a largura da parede: '))

parede = altura * largura
tinta = parede / 2

print(f'Sua parede mede {parede:.1f} metros quadrados.\nPara pinta-la será necessário {tinta:.2f}l de tinta')

