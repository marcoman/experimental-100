# Ask the total bill
# Ask how many people
# Ask how much the tip percentages should be
# Report what each person needs to pay

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
print (f'Each person should pay: ${(bill * (1 + tip / 100)) / people:.2f} \n')