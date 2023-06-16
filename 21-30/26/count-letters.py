sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# I compbine the creation of the list, via split(), with the dict comprehension
result = {word:len(word) for word in sentence.split()}
print(result)

