# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

def calculate_total_rental_cost(pd, pkm, da, kmr):
    """
    pd = price per day
    pkm = price per km
    da = days
    kmr = kilometers driven
    """
    total = pd * da + pkm * kmr
    return f'{total:.2f}'


model_options = """
[1] - Renault Kwid
[2] - Ford Focus
[3] - Volkswagen Golf
[4] - Chevrolet Onix Premier
[5] - Fiat Fastback
[6] - Toyota Corolla
[7] - Jeep Compass
"""

car_models = {
    1: {'model': 'Renault Kwid', 'price_per_day': 150, 'price_per_km': 0.35},
    2: {'model': 'Ford Focus', 'price_per_day': 190, 'price_per_km': 0.40},
    3: {'model': 'Volkswagen Golf', 'price_per_day': 220, 'price_per_km': 0.50},
    4: {'model': 'Chevrolet Onix Premier', 'price_per_day': 260, 'price_per_km': 0.50},
    5: {'model': 'Fiat Fastback', 'price_per_day': 290, 'price_per_km': 0.70},
    6: {'model': 'Toyota Corolla', 'price_per_day': 310, 'price_per_km': 0.90},
    7: {'model': 'Jeep Compass', 'price_per_day': 350, 'price_per_km': 0.60},
}

print(f'{" Car Rental ":-^50}')

days_rented = int(input('Days rented: '))
kilometers_driven = float(input('Kilometers driven: '))
chosen_model = int(input(f'Select the model.\n{model_options}\n:'))

if chosen_model in car_models:
    model_info = car_models[chosen_model]
    total_rental_cost = calculate_total_rental_cost(model_info['price_per_day'], model_info['price_per_km'],
                                                    days_rented, kilometers_driven)
    print(f'\nThe total amount to pay is $ {total_rental_cost}.')
else:
    print('\nInvalid model. Please choose a valid model.')
