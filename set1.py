a={1,2,4,5,4}
print(a)

numbers = {10, 20, 30, 40, 50}
print(numbers)
#Q2. Remove duplicate values from a list.
numbers = [1, 2, 2, 3, 4, 4, 5]
result = set(numbers)
print(result)

#Q3. Find the common elements between two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)


#Q4. Find all unique elements from two sets.
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

#Q5. Find elements present in A but not in B.
a = {10, 20, 30, 40}
b = {30, 40, 50}

print(a - b)
#Q6. Find elements that exist in exactly one of the two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a ^ b)

#Check whether two sets have any common elements.
a = {1, 2, 3}
b = {4, 5, 6}

if a.isdisjoint(b):
    print("No common elements")
else:
    print("Common elements exist")