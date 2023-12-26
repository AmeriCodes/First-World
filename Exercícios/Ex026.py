# Faça um programa que leia uma frase pelo teclado e mostre :
# 1 - Quantas vezes aparece a letra "A"
# 2 - Em que posição ela aparece pela primeira vez.
# 3 - Em que posição ela aparece pela última vez.

sentence = str(input('Enter a sentence for analysis: ')).strip().upper()

print(f'In your sentence, there are {sentence.count("A")} occurrences of the letter "A".')
print(f'The first occurrence of the letter "A" is at position {sentence.find("A")+1}.')
print(f'The last occurrence of the letter "A" is at position {sentence.rfind("A")+1}.')
