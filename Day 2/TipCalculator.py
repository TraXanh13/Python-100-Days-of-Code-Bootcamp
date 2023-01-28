#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total = input("what is the bill cost?\n")
tip = input("How much are you tipping? (whole number: 12% = 12)\n")
numPeople = int(input("How many people are splitting the bill?\n"))

totalWithTip = float(total) * (1 + int(tip) / 100)

print(f'Total w/ Tip : {totalWithTip:,.2f}')
print(f'Each person pays: {totalWithTip / numPeople:.2f}')
