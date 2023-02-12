#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности.

import random

#spisok =[]
#a = int(input("Введите длину списка: "))
#for i in range(a):
#    spisok.append(random.randint(1,10))
#print(f"Создан новый список: \n {spisok}")

#unique_numbers =set(spisok)
#list_of_unique_numbers =[]
#for number in unique_numbers:
#    list_of_unique_numbers.append(number)
#print(list_of_unique_numbers)

def get_unique_elements(sequence):
    unique_elements = []
    for element in sequence:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

sequence = [1, 2, 3, 4, 5, 1, 2, 3, 4]
print(get_unique_elements(sequence))