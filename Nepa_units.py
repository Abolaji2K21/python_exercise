

Nepa_units = int(input("Enter the number of units used: "))

newunit = 0
newunit1 = (Nepa_units - 100) * 10
newunit2 = 100 * 10 + (Nepa_units - 200) * 20


if Nepa_units < 0:
    print("Please enter a valid number of units.")

if Nepa_units <= 100:
    print("You Are Still On A Free Charge Zone:", newunit)

if Nepa_units > 100 and Nepa_units <= 200:
    print("Here is your new unit:", newunit1)

if Nepa_units > 200:
    print("Here is your new unit:", newunit2)

