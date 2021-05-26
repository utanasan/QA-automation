# Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.

def tribonacci(n):
    prev,curr,next=0,0,1
    for i in range(n):
       prev,curr,next=curr,next,prev+curr+next
       yield prev

tr35=tribonacci(35)
print(list(tr35))
