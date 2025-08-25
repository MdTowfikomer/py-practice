
# Empty list
lst = []

# List with elements
lst = [10, 20, 30, 40, 50]

# Access by index
print(lst[0]) # 10
print(lst[-1]) # 50

#Slicing 
print(lst[1:3]) # 20, 30
print(lst[::-1]) # 50, 40, 30, 20, 10

# BASIC_OPERATIONS

_lst1 = [1,2,3]

#add elemets
_lst1.append(4) # 1,2,3,4
_lst1.insert(1,10) #1, 10, 2, 3, 4

#extend with another list
_lst1.extend([5,6])

#remove elements
_lst1.remove(10) # remove by value -> 1, 2,3,4, 5, 6
_lst1.pop() # last element is popped -> 1,2,3,4,5
_lst1.pop(0) # removes index element -> 2,3,4,5

#Delete multiple items
del _lst1[1:3] # deleted elements are 3,4

_lst1.clear() # []


# MERGING LIST WITH ANOTHER COLLECTIONS LIKE SET AND TUPLE

_lst2 = [1,2]
_tple = (3,4)


_lst2.extend(_tple)
print(_lst2)