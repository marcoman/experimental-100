def  add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

functions = {'+' : add,
             '-' : subtract, 
             '*' : multiply, 
             '/' : divide
            }


print (add(1,2))
print (subtract(1,2))
print (multiply(1,2))   
print (divide(1,2))

for i in functions:
    print (functions[i](1,2))


def prompt_user():
    print("Please select an operation: ")
    print("+ Add")
    print("- Subtract")
    print("* Multiply")
    print("/ Divide")
    print("q quit")
    return input()

def  get_number(prompt):
    return int(input(f"Enter {prompt} number: "))

def calculate():
    keep_asking = True
    while keep_asking:
        num1 = get_number("first")
        num2 = get_number("second")
        operator = prompt_user()
        if operator == 'q':
            return
        answer = functions[operator](num1,num2)
        print(f"Answer is {answer}")

calculate()