list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

first_only = set1 - set2

unique = set1 | set2

print("Common elements:", common)
print("Elements only in first list:", first_only)
print("All unique elements:", unique)
