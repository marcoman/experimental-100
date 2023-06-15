#David Beckham
#Victoria Beckham
# 45

#Han Solo
#Princess Leia Organa
# 47

#Pierre Curie
#Marie Curie
# 125

#Mark Antony
#Cleopatra
# 54

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_count = 0
name2_count = 0

for i in name1.lower():
    # print (i)
    if i in 'true':
        # print (f'T{i}')
        name1_count += 1
    if i in 'love':
        # print (f'L{i}')
        name2_count += 1

for i in name2.lower():
    # print (i)
    if i in 'true':
        # print (f'T{i}')
        name1_count += 1
    if i in 'love':
        # print (f'L{i}')
        name2_count += 1

#print (f"name1 is {name1_count} name2 is {name2_count}")

score = name1_count * 10 + name2_count

message = (f'Your score is **{score}**')
if (score < 10 or score > 90):
    message += f', you go together like code and mentos.'
elif (score > 40 and score < 50):
    message += f', you are alrght together.'
else:
    message += f'.'

print (message)
