
age = int(input("Enter your age: "))

max_heartrate = 220 - age

min_targetrate = 0.5 * max_heartrate
max_targetrate = 0.85 * max_heartrate

print("\nResults:")
print("Your maximum heart rate is:", max_heartrate, "beats per minute")
print("Your target heart rate range is:", (min_targetrate), "to", round(max_targetrate), "beats per minute")
