def encode(input, shift):
    output=[]
    for char in input:
        output.append(chr(ord(char)+shift))
    return ''.join(output)

def decode(input, shift):
    output=[]
    for char in input:
        output.append(chr(ord(char)-shift))
    return ''.join(output)


keep_working = True
while keep_working:

    print (f"Type 'encode' to encode, type 'decode' to decode")
    command = input("> ").lower()

    if command == "encode":
        print("Enter the message you want to encode:")
        message = input("> ")
        print("Enter the shift number:")
        shift = int(input("> "))
        print(encode(message, shift))
        print()
    elif command == "decode":
        print("Enter the message you want to decode:")
        message = input("> ")
        print("Enter the shift number:")
        shift = int(input("> "))
        print(decode(message, shift))
        print()
    else:
        print("Invalid command")
        print()
        keep_working = False
