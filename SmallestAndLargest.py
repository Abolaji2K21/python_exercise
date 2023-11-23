print('Arithmetic Smallest and Largest\n')

userInputA=int(input('ENTER INPUT OF ANY CHOICE A: '))

userInputB=int(input('ENTER INPUT OF ANY CHOICE B: '))

userInputC=int(input('ENTER INPUT OF ANY CHOICE C: '))

print('SUMMATION OF ALL THREE INPUT =', userInputA + userInputB + userInputC)


print('AVERAGE OF ALL THREE INPUT =', ((userInputA + userInputB + userInputC)/3))


print('PRODUCT OF ALL THREE INPUT =', userInputA * userInputB * userInputC)

smallest = min(userInputA, userInputB, userInputC)
largest = max(userInputA, userInputB, userInputC)


print('SMALLEST OF ALL THREE INPUT =', smallest)

print('LARGEST OF ALL THREE INPUT =', largest)


