# Crie um programa que leia o nome de uma cidade e diga se ela começa o não com o nome "SANTO".

cidade = str(input('Digite o nome de sua cidade natal: ')).strip().upper().split()

print(cidade[0] == 'SANTO') # Utilizar o .split() é a melhor maneira pôs o programa não entendera como verdadeiro cidades como 'Santos', ou 'Santorini' assim como as outras opções abaixo.


# Outra maneira pode ser
# *print('SANTO' in cidade[0])*

# Ou
"""
cidade = str(input('Digite o nome de sua cidade natal: ')).strip().upper()
print(cidade[:5] == 'SANTO')"""
