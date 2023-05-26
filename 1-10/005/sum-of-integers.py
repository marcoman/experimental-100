smallest = int(input("Enter the smallest number: "))
largest = int(input("Enter the largest number: "))
sum = 0
for i in range(smallest, largest + 1):
    sum += i

print("The sum is", sum)
