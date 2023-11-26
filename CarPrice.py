CarPrice = float(input("Enter the price of the car: "))


if CarPrice < 1000000:
    RoadTaxPercentage = 10
elif 1000000 <= CarPrice < 3000000:
    RoadTaxPercentage = 15
elif 3000000 <= CarPrice < 5000000:
    RoadTaxPercentage = 20
else:
    RoadTaxPercentage = 25

RoadTaxAmount = (RoadTaxPercentage / 100) * CarPrice

print(" AMOUNT TO PAY FOR TAX : ", RoadTaxAmount)


