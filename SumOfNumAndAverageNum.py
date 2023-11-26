number = float(input("Enter Any Number Of Your Choice : "))
total = 0
count = 0
while number != -1:
	total += number
	count += 1
	number = float(input("Enter Any Number Of Your Choice : "))

print("Sum Of All Number Entered Is : ", total)
average = total / count 
print("The Average Number Entered is:", average)