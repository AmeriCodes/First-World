# Crie um script Python que leia dois números e tente mostrar a soma entre eles.



first_value = second_value = ''

while True:
    first_value = str(input('Enter a value: ')).strip()
    try:
        first_value = int(first_value)
        break
    except ValueError:
        try:
            first_value = float(first_value)
            break
        except ValueError:
            print('Invalid value, try again.')
            continue

while True:
    second_value = str(input('Enter another value: ')).strip()
    try:
        second_value = int(second_value)
        break
    except ValueError:
        try:
            second_value = float(second_value)
            break
        except ValueError:
            print('Invalid value, try again.')
            continue

print(f'The sum of {first_value} and {second_value} is {first_value + second_value}')

