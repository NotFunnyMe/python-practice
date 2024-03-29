ice_cream_flavors = ("vanilla", "chocolate", "strawberry", "mint", "caramel")
print(ice_cream_flavors)    # Printing the tuple

for flavors in ice_cream_flavors: # Looping through the tuple
    print(flavors)

print(ice_cream_flavors[0])  # Accessing the first element of tuple 

print(ice_cream_flavors[1])  # Accessing the second element of tuple

ice_cream_flavors[2] = "blueberry" # Trying to change the value of tuple element, it will raise an error.

toy = ("car", "doll", "ball", "puzzle", "blocks")   # A tuple with five elements
print(len(toy)) # Printing the length of tuple
print(toy.count("car")) # Counting the number of times "car" appears in the tuple

toy = (1,2,3,2,3,1,3,2,5) #previous one get deleted and new tuple is created
print(toy.count(3)) # Counting the number of times "3" appears in the tuple
print(toy.index(3)) # Finding the index of first occurrence of "3" in the tuple

rainbow = ("red", "orange", "yellow", "green", "blue", "indigo", "violet") # A tuple with seven elements
