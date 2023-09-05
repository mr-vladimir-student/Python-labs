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
