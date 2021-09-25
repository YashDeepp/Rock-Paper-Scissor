import random as rd
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
choices=["Rock","Paper","Scissors"]
images=[rock,paper,scissors]
choice=int(input("Choose 0 for Rock,1 for Paper Or 2 for Scissors "))
print(choices[choice])
print(images[choice])
a=rd.randint(0,2)
print(f"The system chosed {choices[a]}")
print(images[a])
if((choice==0 and a==1) or (choice==1 and a==2) or (choice==2 and a==0)):
    print("You Lose")
elif(choice==a):
    print("Draw")
else:
    print("You Won")
