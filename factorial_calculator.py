number = int(input("Введите целое число: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print("Факториал числа", number, "равен", factorial)
