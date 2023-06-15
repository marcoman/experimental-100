import math

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (int(math.ceil(float(weight) / ((float (height))**2))))

output = f'Your BMI is {bmi}, you '
if (bmi < 18.5):
    output += "are underweight."
elif (bmi < 25):
    output += "have a normal weight."
elif (bmi < 30):
    output += "are slightly overweight."
elif (bmi < 35):
    output += "are obese."
else:
    output += "are clinically obese."

print (output)
