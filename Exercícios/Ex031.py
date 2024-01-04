# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

def calculate_final_cost(distance, rate):
    return distance * rate

def main():
    try:
        distance_in_km = int(input('Enter the distance of the trip in km: '))
    except ValueError:
        print("Invalid input. Please enter a valid integer for distance.")
        return

    if distance_in_km > 200:
        final_cost = calculate_final_cost(distance_in_km, 0.45)
        print(f'The final cost is {final_cost:.2f} R$.')
    else:
        final_cost = calculate_final_cost(distance_in_km, 0.50)
        print(f'The final cost is {final_cost:.2f} R$.')

if __name__ == "__main__":
    main()
