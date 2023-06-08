

mydict = { 'bug' : 'an error in a program that prevents the program from running as expected',
           'function' : 'a piece of code that you can easily call over and over again',
           'loop' : 'the action of doing something over and over again',
           'list' : 'a collection of items in a particular order',
           'dictionary' : 'a collection of key-value pairs',
           'tuple' : 'a collection of items in a particular order',
           'set' : 'a collection of items in a particular order',
           'string' : 'a series of characters',
           'integer' : 'a whole number',
}


def print_python_item(itemname):
    if itemname in mydict:
        return (f'the definition of {itemname} is {mydict[itemname]}')
    else:
        return (f"I don't know the word {itemname}")  
    

print(print_python_item('bug'))
print(print_python_item('function'))
print(print_python_item('loop'))
print(print_python_item('list'))
print(print_python_item('dictionary'))
print(print_python_item('tuple'))
print(print_python_item('set'))
print(print_python_item('string'))
print(print_python_item('integer'))
print(print_python_item('marco'))


for thing in mydict:
    # This only prints the keys, not the values
    print(thing)
    print (mydict[thing])
    