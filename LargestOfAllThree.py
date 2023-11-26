print('Largest Of All Three \n')

userInputA=int(input('ENTER INPUT OF ANY CHOICE A: '))

userInputB=int(input('ENTER INPUT OF ANY CHOICE B: '))

userInputC=int(input('ENTER INPUT OF ANY CHOICE C: '))


if (userInputA > userInputB):
	if (userInputA > userInputC):
			print('LARGEST OF ALL THREE INPUT =', userInputA)

if (userInputB > userInputA):
	if (userInputB > userInputC):
			print('LARGEST OF ALL THREE INPUT =', userInputB)

if (userInputC > userInputA):
	if (userInputC > userInputB):
			print('LARGEST OF ALL THREE INPUT =', userInputC)
	

	
