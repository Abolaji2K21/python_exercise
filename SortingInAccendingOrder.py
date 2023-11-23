
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 <= num2 and num2 <= num3:
    result = (num1, num2, num3)
if num1 <= num3 and num3 <= num2:
    result = (num1, num3, num2)
if num2 <= num1 and num1 <= num3:
    result = (num2, num1, num3)
if num2 <= num3 and num3 <= num1:
    result = (num2, num3, num1)
if num3 <= num1 and num1 <= num2:
    result = (num3, num1, num2)
if num3 <= num2 and num2 <= num1:
    result = (num3, num2, num1)

print("Numbers in increasing order:", result)
