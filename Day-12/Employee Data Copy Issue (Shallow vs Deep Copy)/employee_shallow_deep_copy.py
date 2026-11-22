import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

# Create shallow copy
shallow_copy = copy.copy(employees)

# Modify nested list
employees[0][1] = "Z"

print("Original:", employees)
print("Shallow copy:", shallow_copy)

# Create deep copy
deep_copy = copy.deepcopy(employees)

# Modify original again
employees[0][1] = "X"

print("Original after modification:", employees)
print("Deep copy:", deep_copy)
