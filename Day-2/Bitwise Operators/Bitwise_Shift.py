num = int(input("Enter a number: "))
shift = int(input("Enter number of positions to shift: "))

left_result = num << shift
right_result = num >> shift

print("Left Shift result:", left_result)
print("Right Shift result:", right_result)
