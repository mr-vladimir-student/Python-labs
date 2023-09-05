# First Task Code

import math

def expression(x):
  z = (2 * math.tan(x) - math.sqrt(x)) / 2
  return z


def sum(x, y):
  sum = 0
  for i in range(x, y + 1):
    if i % 3 == 0:
      sum += i
  return sum

x = float(input("Enter the value for x to calculate z: "))
print("z = ", expression(x))

x = int(input("Enter the first number (x) for the range to calculate sum: "))
y = int(input("Enter the second number (y) for the range to calculate sum: "))

while x > y:

  x = int(input("Please, enter the valid range (first number < second number): "))

  y = int(input("Enter the endpoint in the range: "))

print("The sum of nuumbers (divisible by three) in the range x... y is: ",sum(x, y))



# Second Task Code

from mod import sum

x = int(input("Enter the first number (x) for the range to calculate sum: "))
y = int(input("Enter the second number (y) for the range to calculate sum: "))

while x > y:

  x = int(input("Please, enter the valid range (first number < second number): "))

  y = int(input("Enter the endpoint in the range: "))

print("The sum of nuumbers (divisible by three) in the range x... y is: ",sum(x, y))

