def greet_with_name(name):
    print("Hello ", name)
    print(f"How are you {name}?")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

def greet_pos(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Joe", "Chicago")
greet_with("Jack Bauer", "classified")
greet_with("classified", "Jack Bauer")
greet_with(location="classified", name="Jack Bauer")
greet_with(location="New York City", name="Rudy")