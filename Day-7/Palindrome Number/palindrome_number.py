#Write a program to check whether a number is a Palindrome. num = int(input("Enter a number: "))
num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print(num, "is a Palindrome number")
else:
    print(num, "is not a Palindrome number")
