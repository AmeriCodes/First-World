# Crie um programa que leia o nome de uma cidade e diga se ela começa o não com o nome "SANTO".

city = str(input("Enter your home city: ")).strip()

print(city[:5].title() == 'Santo')
