# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input('Is that a leap year? Enter to know: '))

if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
