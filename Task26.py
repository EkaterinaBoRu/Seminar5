"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """

def degreeNumber (A, B):
    if B in range(0,1):
        return 1
    else:
        for i in range(1, B+1):
            result = degreeNumber(A, B-1)*A
        return result

A = int(input("Введите положительное основание А: "))
B = int(input("Введите неотрицаткльную целую степень B: "))

print(degreeNumber(A,B))