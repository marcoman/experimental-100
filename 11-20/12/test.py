enemies = 1

def increase_enemies():
    enemies =2 
    print (f'Enemies inside function {enemies}')

increase_enemies()
print (f'Enemeies outside function {enemies}')

player_health = 10

def drink_potion():
    # This variable is only available inside this function.
    potion_strength = 2
    print (potion_strength)

drink_potion()
print (player_health)


if 3>2:
    a = 12

# This next variable is available, as there is no block scope.
print (a)

enemies = "skeleton"
def inc_enemies():
    enemies = "zombie"
    print (f'enemies inside func {enemies}')

inc_enemies()
print(f'enemies outside function {enemies}')