# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum = 0
count = 0
for n in student_heights:
  sum += n
  count += 1
print (f'sum is {sum}, count is {count}')
print (f'average is {sum/count}')


