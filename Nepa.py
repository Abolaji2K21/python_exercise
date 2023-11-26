

Nepa_units = int(input("Enter the number of units used: "))
    
if units < 0:
    print("Please enter a valid number of units.")
else:
if units <= 100:
   newunit = 0
else if units <= 200:
   newunit = (units - 100) * 10
else:
   newunit = 100 * 10 + (units - 200) * 20

        print(f"Electricity Bill: {bill_amount} naira")
except ValueError:
    print("Please enter a valid number.")
