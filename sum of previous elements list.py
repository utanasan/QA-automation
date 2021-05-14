# Найти для каждого элемента списка А сумму предыдущих элементов и записать эти суммы в новый
# список B.


import random
n=int(input("Введите размер списка:"))
A=[]
B=[]
for i in range(n):
    a=random.randint(0,100)
    A.append(a)
print(f"Список A: {A}")
for i in range (len(A)):
    b=sum(A[0:i+1])
    B.append(b)
print(f"Новый список B - сумма предыдущих элементов: {B}")

