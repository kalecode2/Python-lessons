bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0].title())
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
motorcycles.append("honda")
print(motorcycles)
motorcycles = []
print(motorcycles)
motorcycles.append("yamaha")
motorcycles.append("ducati")
motorcycles.append("honda")
motorcycles.append("suziki")
print(motorcycles)
del motorcycles[3]
print(f"new list is {motorcycles}")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
   print(f"{magician.title()} that was a great trick!")
   print(f"I can't wait to see your next trick {magician.title()}")
print("Thank you, everyone. That was a great magic show!")

for value in range(1, 10):
   print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
   square = value ** 2
   squares.append(square)
print(squares)

# It works the same as upper.
squares = [value**2 for value in range(1, 11)]
print(squares)