def my_function(number1, number2):
    return number1 + number2

def format_name (fname, lname):
    fname = fname.title()
    lname = lname.title()
    print (f'Your name is {fname} {lname}')



def format_name_2 (fname, lname):
    if fname == "" or lname == "":
        return "You didn't provide valid inputs"
    fname = fname.title()
    lname = lname.title()
    return f'Your name is {fname} {lname}'


print (my_function(2, 3))
print (my_function(2, 31))

format_name('john', 'doe')
format_name('jane', 'DOE')
format_name('JOHN', 'doe')
format_name('JANE', 'DOE')

format_name_2('', '')
format_name_2(lname = 'DOE', fname='')
