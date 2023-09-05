# First Task Code

t = str(input("Enter a string (min-lenth: 19symbols): "))

while (len(t)) < 19:
  print("The line is too short to cut. Please try again!")

print("The result of the cut:", t[18::4])

# Second Task Code

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

setWord1 = set(word1.lower())
setWord2 = set(word2.lower())

if setWord1.issubset(setWord2):
  print(
      f"All letters from the word '{word1}' are present in the word '{word2}'."
  )
else:
  print(
      f"Not all letters from the word '{word1}' are present in the word '{word2}'."
  )

# Third Task Code 

s = str(input("Enter a sentance: "))

words = s.split()

longestWord = max(words, key = len)
print(f"The longest word here is: {longestWord}")
