# Program to find the ASCII value of a character

# Take input from user
char = input("Enter a character: ")

# Check if exactly one character was entered
if len(char) == 1:
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}")
else:
    print("Please enter exactly one character.")