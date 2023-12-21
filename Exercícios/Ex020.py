# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

students = []

number_of_students = int(input('How many students do you want to shuffle? : '))

for i in range(1, number_of_students + 1):
    student = input(f"Enter the {i}º student: ")
    students.append(student)

random.shuffle(students)

print("Shuffled list of students:", students)
