# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. ps: fiz este exercicio utilizando a cotação do dia. . .

import os

def convert_currency(value, rate):
    return value * rate


rates = {'real': 4.91, 'dollar': 1.0, 'pound': 0.79, 'euro': 0.93}

print(f'{" Currency Converter ":=^52}')

while True:
    base_currency = input("Enter the base currency (real, dollar, pound, euro): ").lower()

    if base_currency not in rates:
        os.system('clear')
        print("Invalid base currency. Please try again.")
        continue

    try:
        amount = float(input(f"Enter the amount in {base_currency}: "))
    except ValueError:
        os.system('clear')
        print("Invalid value. Please try again.")
        continue

    target_currency = input("Enter the target currency (real, dollar, pound, euro): ").lower()

    if target_currency not in rates:
        os.system('clear')
        print("Invalid target currency. Please try again.")
        continue

    converted_amount = convert_currency(amount, rates[target_currency] / rates[base_currency])

    print(f"\n{amount} {base_currency.upper()} is equivalent to {converted_amount:.2f} {target_currency.upper()}")

    continue_prompt = input("\nDo you want to make another conversion? (yes/no): ").lower()
    if continue_prompt != 'yes':
        break

print("Thank you for using the currency converter. Goodbye!")
