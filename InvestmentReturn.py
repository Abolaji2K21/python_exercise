print('Investment Return: \n')

userInputp=int(input('ENTER THE ORIGINAL AMOUNT INVESTED: \n'))
userInputr=int(input('ENTER THE ANNUAL RATE OF RETURN: \n'))
userInputn=int(input('ENTER THE NUMBER OF YEARS: \n'))


userInputR= userInputr / 100

userInputq= 1 + userInputR

Result= (userInputp * (userInputq ** userInputn))


print(Result)


