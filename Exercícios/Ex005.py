# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.



while True:
    entry = str(input('Type a number: ')).strip()

    try:
        entry = int(entry)
        break
    except:
        try:
            entry = float(entry)
            break
        except:
            print('Invalid entry, enter a number.')
            continue

successor = entry + 1
predecessor = entry - 1

print(f'The predecessor of {entry} is {predecessor}.')
print(f'The successor of {entry} is {successor}.')