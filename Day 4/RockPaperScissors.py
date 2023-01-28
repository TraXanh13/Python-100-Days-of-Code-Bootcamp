import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
moves = {'r': rock, 'p': paper, 's': scissors}

pMove = input("Play (R)ock, (P)aper, (S)cissors?").lower()
cMove = random.choice(list(moves.keys()))

if (pMove in moves):
    print(f'Your Move:\n{moves[pMove]}\nComputer Move:\n{moves[cMove]}')

    if (pMove == 'r' and cMove == 's' or pMove == 'p' and cMove == 'r'
            or pMove == 's' and cMove == 'p'):
        print("You Won!")
    elif (pMove == cMove):
        print("You Tied!")
    else:
        print("You Lost!")
else:
    print('Invalid choice... You lose')
