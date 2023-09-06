# First task code

N = int(input("Enter the number of elements in array: "))
arr = []

for i in range(N):
  num = int(input(f"Enter the {i+1} element: "))
  arr.append(num)

maxPositive = None

for num in arr:
  if num > 0 and (maxPositive is None or num > maxPositive):
    maxPositive = num

if maxPositive is not None:
  print(f"The largest positive element is: {maxPositive}")
else:
  print("The array doesn't have any positive elements")

# Second task code

n = 7

a = [[(n - i + j) * (i >= j) for i in range(n-1, -1, -1)] for j in range(n)]

for r in a:
  print(*r)
