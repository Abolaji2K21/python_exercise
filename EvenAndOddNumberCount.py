numbers = range(1, 101)

evenCount = 0
oddCount = 0

for num in numbers:
    if num % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print("Number of even numbers:", evenCount)
print("Number of odd numbers:", oddCount)
