''' 
we take two files (file1 and file2) and compare their contents.
We next print the list common entries.
These two files contain numbers, in no particular order'''

file1 = "file1.txt"
file2 = "file2.txt"

with open(file1) as f:
    file1_list = f.readlines()

with open(file2) as f:
    file2_list = f.readlines()

result = [int(item.strip()) for item in file1_list if item in file2_list] 



# Write your code above 👆

print(result)


