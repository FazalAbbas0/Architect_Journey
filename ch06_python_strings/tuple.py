# Tuples
# A tuples is immutable sequence of variables. They are similar to lists but they can not be changed after creation. They are defined with parantheses () in stead of [].
# Tuples are often used to store related data that should not be changed, such as coordinates, RGB values, etc. 
# Creating a tuple
my_tuple = ("apple", 125, 1.25, False)
print(my_tuple)
print(len(my_tuple))
# Accessing tuple items
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])
# Tuples are immutable, we can not change the items in a tuple after it is created. We can not add, remove or change items in a tuple.
# my_tuple[0] = "banana" # This will raise an error because tuples are immutable. We can not change the items in a tuple after it is created. We can not add, remove or change items in a tuple.
# Variable types data entry in a tuple
tuple_1 = ("apple", "banana", "orange")
tuple_2 = (1, 5, 7, 9, 3)
tuple_3 = (True, False, True)
tuple_4 = ("abc", 34, True, 40, "male")
tuple_5 = ("Pineapple", "Mango", "Grapes", "Watermelon", "Strawberry")

print(tuple_1)
print(tuple_2)
print(tuple_3)
print(tuple_4)
print(tuple_5)
