alien_0 = {
   'color': 'green',
   'points': 5
}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

alien_0['x_position'] = 0
alien_0['y-position'] = 25
print(alien_0)

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"Now, the alien is {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
   x_increment = 1
elif alien_0['speed'] == 'medium':
   x_increment = 2
else:
   # This must be a fast alien.
   x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

favorite_languages = {
   'jen': 'python',
   'sarah': 'c++',
   'edward': 'rust',
   'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah 's favorite language is {language.title()}")

user_0 = {
   'username': 'efermi',
   'first': 'enrico',
   'last': 'fermi',
}
for key, value in user_0.items():
   print(f"\nKey: {key}")
   print(f"Value: {value}")

for name, language in favorite_languages.items():
   print(f"{name.title()}'s favorite language is {language.title()}.")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
   print(f"Hey {name.title()},")
   if name in friends:
      language = favorite_languages[name].title()
      print(f"\t{name.title()}, I see you love {language.title()}.")


# Nesting in dictionaries.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
   print(alien)

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien in range(30):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)

for alien in aliens[:3]:
   if alien['color'] == 'green':
      alien['color'] = 'yellow'
      alien['speed'] = 'medium'
      alien['points'] = 10
   elif alien['color'] == 'yellow':
      alien['color'] = 'red'
      alien['speed'] = 'fast'
      alien['points'] = 15

# Show the  first 5 aliens
for alien in aliens[:5]:
   print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Store information about a pizza being ordered.
pizza = {
   'crust': 'thick',
   'toppings': ['mushrooms', 'extra cheese']
}
# Summarise the order.
print(f"You ordered a {pizza['crust']} -crust pizza with the following toppings:")
for topping in pizza['toppings']:
   print(f"\t{topping.title()}")
