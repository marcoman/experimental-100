# age check
# photo check

bill = 0
height = int(input("How tall are you in cm? "))

if (height < 120):
    print("You are not tall enough to ride")
else:
    print("You are tall enough to ride")

    age = int(input("What is your age? "))

    if age < 12:
        bill += 5
        print("You pay $5")
    if age < 18:
        bill += 7
        print("You pay $7")
    else:
        bill += 12
        print("You pay $12")

    photo = input("Do you want a photo? Y or N ")
    if photo == 'Y' or photo == 'y':
        bill += 3
        print("You pay $3")

    print("Your final bill is $" + str(bill) + " Thank you")
