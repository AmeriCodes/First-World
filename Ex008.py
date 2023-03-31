# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e minímetros
print('==' * 15)
m = float(input('Digite uma medida em metros: '))
print('==' * 15)

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'A medida de {m}metros corresponde a: \n{km} quilômetros \n{hm} hectômetros \n{dam} decâmetros \n{dm:.0f} decímetros \n{cm:.0f} centímetros \n{mm:.0f} milímetros')
