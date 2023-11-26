print('Checking To See If Numbers in Range 1500 to 2701 are Divisible by 5 and 7: ')

for number in range(1500, 2701):
    if number % 5 == 0 and number % 7 == 0:
        print(number, end=" ")
