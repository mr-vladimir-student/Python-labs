# First Task Code
def removeEvenIndexElements(inputList):
  return [inputList[i] for i in range(len(inputList)) if i % 2 == 0]

userInput = input("Enter a list of numbers separated by spaces: ")
inputList = [int(x) for x in userInput.split()]

newList = removeEvenIndexElements(inputList)

print("List without elements at even indices:", newList)

# Second Task Code

def reverseAndPrintList(inputList):
  reversedList = inputList[::-1]  
  print("List in reverse order:", reversedList)

userInput = input("Enter a list of elements separated by spaces: ")
inputList = userInput.split()

reverseAndPrintList(inputList)

# Third Task Code

def processText(text):
  charSet = {char for char in text if char.isalpha()}
  punctuationCount = sum(1 for char in text if char not in charSet and not char.isspace())
  return charSet, punctuationCount


userInput = input("Enter text in lowercase Latin letters: ")
resultSet, punctuationCount = processText(userInput)

print("Set of letters present in the text:", resultSet)

if len(resultSet) == 0:
  print("The set is empty")
else:
  print("Number of punctuation marks in the text:", punctuationCount)
