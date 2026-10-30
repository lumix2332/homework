import random

secret_number = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. Спробуйте вгадати його за 3 спроби.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба {attempt}: Введіть число: "))

    if guess == secret_number:
        print("Вітаю! Ви вгадали число!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Ви використали всі спроби. Я загадав число: {secret_number}")