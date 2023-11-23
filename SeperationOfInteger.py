print('Separating the Digits in an Integer: \n')


userInput= int(input('ENTER ANY FIVE INTEGER OF YOUR CHOICE: \n'))


userInput1 = userInput // 10000
userInput2 = (userInput % 10000) // 1000
userInput3 = (userInput % 1000) // 100
userInput4 = (userInput % 100) // 10
userInput5 = (userInput % 10)

print(f'{userInput1}\t{userInput2}\t{userInput3}\t{userInput4}\t{userInput5}\t')






	




