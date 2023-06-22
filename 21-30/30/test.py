'''
Today we test exceptions.
'''


# File error returns the following when there is no file named test.txt
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# with open('test.txt') as f:
#     print(f.read())

# Let's use exception handling instead
try:
    with open('test.txt') as f:
        print(f.read())
except FileNotFoundError:
    print('We caught the exception!')
    print('File not found')   
except KeyError:
    print('Key error caught')
except Exception as e:
    print(e)
    print('Something else went wrong')
 else:
    # If we don't have an exception, we'll get this
    print('No exception caught')
finally:
    print('This will always run')
    f.close()


