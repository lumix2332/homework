n = int(input("Введіть число n для обчислення факторіала: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факторіал числа {n} дорівнює {factorial}")