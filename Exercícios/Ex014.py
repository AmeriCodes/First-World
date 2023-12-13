# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

print(f'{" Temperature Conversion ":-^47}')

celsius = str(input('Enter the temperature in degrees Celsius (°C): '))
celsius = float(celsius)

fahrenheit = celsius * 1.8 + 32

print(f'\nThe temperature of {celsius}°C is equivalent to {fahrenheit}°F')
