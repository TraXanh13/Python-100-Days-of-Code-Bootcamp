# w writes over previous info - will create a new file
# a adds to the text file
# r reads the file
with open("textFile.txt", "w") as f:
    f.write("This is some text")

with open("textFile.txt", "a") as f:
    f.write("\nAdded some more text")

with open("textFile.txt") as f:
    fileContent = f.read()
    print(fileContent)
