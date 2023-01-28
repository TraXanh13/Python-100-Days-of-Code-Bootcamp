# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

score = 0
combineName = (name1 + name2).lower()

for x in "true":
    score += combineName.count(x)

score *= 10

for x in "love":
    score += combineName.count(x)

if(score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")