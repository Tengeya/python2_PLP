# Create an empty list called my_list
my_list = []

# Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Extend with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of value 30 in my_list:", index_30)

# Print the modified my_list
print("Modified my_list:", my_list)
