# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

if (len(position)==2):
    pos_2 = int(position[0])
    pos_1 = int(position[1])
    if (pos_1 <= 3 and pos_1 > 0 and pos_2 <= 3 and pos_2 > 0):
        map[pos_1-1][pos_2-1] = 'X'
else:
    pass


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

