#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
numlen = len (two_digit_number)
mysum = 0
for d in two_digit_number:
    if (type(d) is str):
        mysum += int(d)

print (f"{mysum}")
