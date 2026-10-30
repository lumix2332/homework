a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
operation = input("Введіть математичну дію (+, -, *, /): ")

if operation == "+":
    result = a + b
    print(f"Результат: {result}")
elif operation == "-":
    result = a - b
    print(f"Результат: {result}")
elif operation == "*":
    result = a * b
    print(f"Результат: {result}")
elif operation == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        result = a / b
        print(f"Результат: {result}")
else:
    print("Помилка: невідома математична дія.")