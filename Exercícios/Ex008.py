# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e minímetros
print('----- Measurement Converter -----')

while True:
    meters = str(input('\nMeters: ')).strip()
    try:
        meters = float(meters)
        break
    except ValueError:
        print('Invalid input!\nPlease try again.')
        continue

kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10
decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000

print('\n----- Successful Conversion -----\n')

print(f'{kilometers=}\n{hectometers=}\n{decameters=}\n{meters=}\n{decimeters=}\n{centimeters=}\n{millimeters=}')

