from flask import Flask
app = Flask(__name__)

# This next line will return "__name__" if we run this directly, and not as a library.
# print (__name__)

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
    def say_hello(self):
        return f"Hello {self.name}"

def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Marco")
new_user.is_logged_in = False
create_blog_post(new_user)

new_user.is_logged_in = True
create_blog_post(new_user)


