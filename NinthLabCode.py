def createTextFile(filename):
    try:
        with open(filename, "w") as file:
            file.write("Hello, World! ")
            file.write("Are you hungry? ")
            file.write("If so, come and get a burger! ")
            file.write("Bon appétit")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"{filename} has been successfully opened")
        print("The data has been successfully written into this file!")


def processAndWriteFile(inputFilename, outputFilename):
  try:
    with open(inputFilename, "r") as inputFile, open(outputFilename,
                                                     "w") as outputFile:
      for line in inputFile:
        words = line.split()
        for word in words:
          if isVowel(word[0]):
            outputFile.write(word + '\n')
  except FileNotFoundError:
    print("Error: File not found.")
  except Exception as e:
    print(f"Error: {e}")
  else:
    print(
        f"The data has been processed and successfully transported to the {outputFilename}!"
    )


def readAndPrintFile(filename):
  try:
    with open(filename, "r") as file:
      print(f"The data in the {filename}: ")
      for line in file:
        print(line.strip())
  except FileNotFoundError:
    print("Error: File not found.")
  except Exception as e:
    print(f"Error: {e}")


def isVowel(letter):
  vowels = "AEIOUaeiou"
  return letter in vowels


createTextFile("TF13_1.txt")
processAndWriteFile("TF13_1.txt", "TF13_2.txt")
readAndPrintFile("TF13_2.txt")
