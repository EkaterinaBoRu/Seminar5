"""Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*
2 2
    4 """

def sum(a,b):
    if a==b==0:
        return 0
    elif a==1:
        return b+1
    elif b==1:
        return a+1
    else:
        return sum(a-1,b+1)
        
a = int(input("Введите целое неотрицательное число а: "))
b = int(input("Введите целое неотрицательное число b: "))

print(sum(a,b))