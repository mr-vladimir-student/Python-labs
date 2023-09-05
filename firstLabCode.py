# First Task Code

# Prompt to enter positive numbers
a = float(input("Enter a positive value for a: "))
b = float(input("Enter a positive value for b: "))

# Check if a and b are positive
if a <= 0 or b <= 0:
    print("Both a and b must be positive numbers.")
else:
    # Calculating x
    if a > b:
        x = a * b + 31
    elif a < b:
        
        x = (a * 5 - 1) / b
    else:
        x = -25
    
    # Displaying the result
    print(f"The value of 'X' is: {x}")


# Second Task Code

print(" x\t    y")
for i in range(0, 9):
    x = i/2
    y = x 
    print(f"{x:.1f}\t   {y:.1f}")


# Third Task Code

# Prompt to enter a number for the rows and columns
n = int(input("Enter a number between 1 and 9: "))
print(" ")

# Printing rows of the first piramid
for i in range(1, n+1):
  
  # Printing spaces for the first piramid
  print(" "*((n*2)-2), end = '')
  
  # Printing the numbers and spaces in each row
  for j in range(i, 0, -1):
    print(j, end = ' ')

  # Moving to the next line after each row
  print()
  
# Printing rows of the second piramid 
for i in range(1, n + 1):
  
    # Printing spaces for the current row
    for j in range(i - 1):
        print(" ", end = ' ')
    
    # Printing the numbers in each row 
    for k in range(1, n - i + 2):
        print(k, end = ' ')
      
    # Moving to the next line after each row
    print()
