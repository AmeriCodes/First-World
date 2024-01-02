# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. Á multa vai custar R$7,00 por cada Km acima do limite.

def calculate_penalty(speed):

    cost_per_excess_km = 7.00
    penalty_amount = (speed - 80) * cost_per_excess_km
    return penalty_amount

velocity = int(input("Enter the car's speed: "))

if velocity <= 80:
    print("Have a nice day, drive safely!")
else:
    print(f"You exceeded 80km, the speed limit!\nThe penalty will be {calculate_penalty(velocity):.2f}R$")
