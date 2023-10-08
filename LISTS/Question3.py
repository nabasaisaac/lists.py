"""Question 3"""
lists = [1, 2, 3, 4, 3, 4, 4, 4, 5, 6, 7, 3, 8, 3, 'tree', 'cow', 'treee', 'tree']
new_list = []
for element in lists:
    if element not in new_list: # Append element to the list as long as it is not already in new_list
        new_list.append(element)

# The goal is to have a list without repeated elements
print(new_list)