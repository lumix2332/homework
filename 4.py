start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

if start <= end:
    for i in range(start, end + 1):
        print(i, end=" ")
else:
    print("Початкове число має бути меншим або рівним кінцевому.")
print()