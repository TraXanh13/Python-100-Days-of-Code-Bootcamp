import random

# Generate a random number between 1 and 100
num = random.randint(1, 101)
guess = -1
difficulty = ""

print("I have chosen a number between 1 and 100")

while difficulty != 'easy' and difficulty != 'hard':
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
  lives = 10

elif difficulty == "hard":
  lives = 5


def check_guess(guess, num, lives):
  if guess == num:
    print("You win!")
  elif guess > num:
    print("Too high")
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number.")
  elif guess < num:
    print("Too low")
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number.")
  return lives


while lives and guess != num:
  guess = int(input("Make a guess: "))
  lives = check_guess(guess, num, lives)
