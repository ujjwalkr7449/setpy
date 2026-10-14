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
    
#Check whether one set is a subset of another.
a = {2, 4}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))
#Find the number of unique elements in a list.
numbers = [1, 2, 2, 3, 3, 3, 4, 5]

unique_numbers = set(numbers)

print(len(unique_numbers))

#Q10. Find duplicate values in a list using sets.
numbers = [1, 2, 3, 2, 4, 5, 1, 6]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)


#Q11. Find missing numbers between 1 and 10.
numbers = {1, 2, 4, 6, 7, 9, 10}

expected = set(range(1, 11))

missing = expected - numbers

print(missing)


#Q12. Check whether two lists contain the same unique elements.
a = [1, 2, 2, 3, 4]
b = [4, 3, 2, 1, 1]

if set(a) == set(b):
    print("Same unique elements")
else:
    print("Different elements")
    
    
#Q13. Find common students in two courses.

python_students = {"Amit", "Rahul", "Priya", "Neha"}
java_students = {"Rahul", "Neha", "Vijay"}

print(python_students.intersection(java_students))