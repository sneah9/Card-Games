import random
from Deck import *

print("WAR: There is only so much within your control!")
user = input("Welcome warrior, enter your name to begin:")
play = input("Shuffle and deal? y/n: ") 

userHand= []
userPlay= []
cpuHand= []
cpuPlay= []

if play == "y":
    print("Your cards are being shuffled and dealt")
    random.shuffle(deck1)
    for i in range(0,len(deck1)-1,2):  
        userHand.append(deck1[i])
        cpuHand.append(deck1[i+1])
    print(userHand, "\n",cpuHand)
    count=0
    #extra=1
    while ((len(userHand)>0) and (len(cpuHand)>0)) or ((len(userPlay)==0)):
        if (len(userPlay)== 0) and (len(cpuPlay)== 0):
            userPlay.append(userHand.pop(0))
            cpuPlay.append(cpuHand.pop(0))
            print(userPlay)
            print(cpuPlay)

        userValue = dict1.get(userPlay[0])
        cpuValue = dict1.get(cpuPlay[0])
        print (userValue)
        print (cpuValue)

        if userValue > cpuValue:
            for x in range(len(userPlay)):
                userHand.append(userPlay.pop(0))
                userHand.append(cpuPlay.pop(0))

        elif userValue < cpuValue:
            for y in range(len(userPlay)):
                cpuHand.append(userPlay.pop(0))
                cpuHand.append(cpuPlay.pop(0))

        else:
            for z in range(4):
                if (len(userHand) != 0) & (len(cpuHand) !=0):
                    userPlay.insert(0, userHand.pop(0))
                    cpuPlay.insert(0, cpuHand.pop(0))
 #           print(userPlay)
  #          print(cpuPlay)
            
        count+=1
        print(userPlay)
        print(cpuPlay)    
        print('You have', len(userHand), 'cards in your hand')
        print('the computer has', len(cpuHand), 'cards in its hand')
        print('end of round', count)

    if userValue > cpuValue:
        for x in range(len(userPlay)):
            userHand.append(userPlay.pop(0))
            userHand.append(cpuPlay.pop(0))

    elif userValue < cpuValue:
        for y in range(len(userPlay)):
            cpuHand.append(userPlay.pop(0))
            cpuHand.append(cpuPlay.pop(0))

    if len(cpuHand) == 0:
        print(user + ', you have won the WAR!')
    else:
        print(user + ', you have lost the WAR!')
    print(userPlay, cpuPlay, len(userPlay), count)

        
else:
    print("Have a great day, come back when you are ready to engage in WAR")
    exit