# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e tadas as informações possíveis sobre ele.


enter = input('Type something: ')

print(f'The primitive type of this value is {type(enter)}')
print(f'Are there only spaces? {enter.isspace()}')
print(f'Is it a number? {enter.isnumeric()}')
print(f'Is it alphabetical? {enter.isalpha()}')
print(f'Is it alphanumeric? {enter.isalnum()}')
print(f'Is it in capital letters? {enter.isupper()}')
print(f'Is it in lowercase? {enter.islower()}')
print(f'Is it captalized? {enter.istitle()}')
