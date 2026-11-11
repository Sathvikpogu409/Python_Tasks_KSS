import calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    result = calculator.add(num1, num2)
    print("Addition:", result)

elif choice == '2':
    result = calculator.subtract(num1, num2)
    print("Subtraction:", result)

elif choice == '3':
    result = calculator.multiply(num1, num2)
    print("Multiplication:", result)

elif choice == '4':
    result = calculator.divide(num1, num2)
    print("Division:", result)

else:
    print("Invalid choice!")
