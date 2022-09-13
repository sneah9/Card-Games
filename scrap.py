import random, sys
from deck import *

print("WAR: There is only so much within your control!")
user = input("Welcome warrior, enter your name to begin:")

# What are user_hand and user_play?
# Some comments might help make this more clear for both of us.

user_hand= []
user_play= []
cpu_hand= []
cpu_play= []

print("Your cards are being shuffled and dealt")
random.shuffle(deck1)

# Deal cards to user and computer

for i in range(0,len(deck1)-1,2):  
  user_hand.append(deck1[i])
  cpu_hand.append(deck1[i+1])

  print('USER HAND SO FAR:', user_hand)
  print('CPU HAND SO FAR:', cpu_hand)


# COUNT used to see how many rounds are needed to complete the game
count=0

while True:
    # If both play piles are empty, add one card to each play pile.
    #
    # Is this check necessary, or do you always make playcards?- if there is a war, you need to compare the hands that exist, not add more cards
  
    if (len(user_play)== 0) and (len(cpu_play)== 0):
        if len(user_hand) == 0 or len(cpu_hand) == 0:
            break
        user_play.append(user_hand.pop(0))
        cpu_play.append(cpu_hand.pop(0))
      
        print('USER PLAY:', user_play)
        print('CPU PLAY:', cpu_play)
  
    user_value = dict1.get(user_play[0])
    cpu_value = dict1.get(cpu_play[0])
  
    print ('USER VALUE:', user_value)
    print ('CPU VALUE:', cpu_value)

    #sys.exit()

    if user_value > cpu_value:
        print('USER VALUE IS GREATER')
        for x in range(len(user_play)):
            user_hand.append(user_play.pop(0))
            user_hand.append(cpu_play.pop(0))

    elif user_value < cpu_value:
        for y in range(len(user_play)):
            cpu_hand.append(user_play.pop(0))
            cpu_hand.append(cpu_play.pop(0))

    elif len(user_hand) == 0 or len(cpu_hand) == 0:
      break

    else:
        for z in range(4):
            if (len(user_hand) != 0) & (len(cpu_hand) !=0):
                user_play.insert(0, user_hand.pop(0))
                cpu_play.insert(0, cpu_hand.pop(0))
  
    count+=1
    print(user_play)
    print(cpu_play)    
    print('You have', len(user_hand), 'cards in your hand')
    print('the computer has', len(cpu_hand), 'cards in its hand')
    print('end of round', count)


if len(cpu_hand) == 0:
    print(user + ', you have won the WAR!')
else:
    print(user + ', you have lost the WAR!')

#print(user_play, cpu_play, len(user_play), count)