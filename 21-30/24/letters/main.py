'''
Mail merge example.  Take files from the input folder and send them to the output folder.


'''
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


file_input_names = "input/Names/invited_names.txt"
file_input_letter = "input/Letters/starting_letter.txt"
file_output_folder = "output/ReadyToSend/"

names = []
with open(file_input_names) as f:
    for name in f:
        name = name.strip('\n')
        names.append(name)
print (names)

with open(file_input_letter) as f:
    letter = f.read()

for name in names:
    temp_letter = letter.replace("[name]", name)

    with open(f'{file_output_folder}/letter-{name}.txt', 'w') as f:
        f.write(temp_letter)

