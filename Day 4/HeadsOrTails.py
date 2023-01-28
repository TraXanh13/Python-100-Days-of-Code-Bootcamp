# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random as rand
# Write the rest of your code below this line 👇
headsTails = rand.randint(0, 1)

if (headsTails):
    print("Heads")
else:
    print("Tails")
