import random

user = input ("what\'s your choice? 'r' for roch, 's' for scissors and 'p' for paper :")
computer = random.choice(['r','p','s'])

if user == computer:
    print ("it's a tie")
elif (user == 'r' and computer == 's') or (user =='p' and computer == 'r') or (user == 's' and computer == 'p'):
    print ("CONGRATULATIONS!! YOU WON.")
else:
    print ("You lost!!")
     




# winning condition r>s or p>r or s>p