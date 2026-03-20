# Exercise 6: Sequences & Loops

# 1. Lists — Create a list of at least five city names. Append a sixth city, sort the list alphabetically,
# then print each city on its own line using a for loop.
cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
cities.append("Berlin")
cities.sort()
print("Cities:")
for city in cities:
    print(city)

# 2. Tuples — Create a list of at least three (x, y) coordinate tuples. Loop through the list and print
# the distance of each point from the origin (use the formula sqrt(x2 + y2); you may import the math
# module).
import math
coordinates = [(3, 4), (1, 1), (0, 5), (6, 8)]
print("\nDistances from origin:")
for x, y in coordinates:
    distance = math.sqrt(x**2 + y**2)
    print(f"Point ({x}, {y}): {distance:.2f}")

# 3. Sets — Create two sets of integers (at least five elements each). Print their union,
# intersection, and difference.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (Set1 - Set2): {set1 - set2}")

# 4. Dictionaries — Create a dictionary mapping at least five country names to their capitals. Ask
# the user to enter a country name and print the corresponding capital. Handle the case where the
# country is not found with a friendly message.
capitals = {
    "USA": "Washington D.C.",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
country = input("\nEnter a country name: ")
if country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")
else:
    print(f"Sorry, I don't have information about the capital of {country}.")
