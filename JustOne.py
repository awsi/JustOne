import os

#https://www.delftstack.com/de/howto/python/python-clear-console/
def clearConsole():
    command = 'clear' if os.name not in ('nt', 'dos') else 'cls'  # If Machine is running on Windows, use cls
    os.system(command)
    
def playagain():
    print ("Play again? (yes/no)")            
    response = input('>')
    if response.lower() == "yes":
        print ("") # restart the game
    else:
        print ("")

print("Hello! Welcome to JustOne! Would you like to know the rules first? (yes/no)")
response = input('>')
if response.lower() == "yes":
    print ('"RULES"')  
    print ('_ _ _ _ _ _ _ _ _ _ _ _ _')
    print ('Please enter the number of players: (ONLY THREE PLAYERS) ')
else:
    print ("Please enter the number of players: (ONLY THREE PLAYERS)") # (Demo: 3 Players , Full Game: up to 7 Players)

Number_Of_Players = input('>')
clearConsole()
while True:
    if Number_Of_Players == "3":
        break
    else:
        print (":( Please restart the Game and enter number 3" )
        clearConsole()
        
        

card1 = ["APPLE", "DOG", "ICE", "ROOM", "CLUB"]
print ("Player 1: Choose a word between 1 and 5 and turn around :)")
response = input('>')

print ("The Mystery word is: ")
Mystry = []

while True:
    if response == "1":
        Mystry = card1[0]
        print (card1[0])
        break
    elif response == "2":
        Mystry = card1[1]
        print (card1[1])
        break
    elif response == "3":
        Mystry = card1[2]
        print (card1[2])
        break
    elif response == "4":
        Mystry = card1[3]
        print (card1[3])
        break
    elif response == "5":
        Mystry = card1[4]
        print (card1[4])
        break
    else:
        print(":( . Please restart the Game and enter a number between 1 and 5 to choose the Mystry Word") #use a loop to make the aktive players enter a number again
        clearConsole()
        

    
print ("Player 3: Eyes closed :)")
print ("Player 2: ُEnter two clue Words:")
p1_c1 = input('>') # Hints cover up
p1_c2 = input('>') # Hints cover up
clearConsole()
print ("Player 2: Eyes closed :)")
print ("Player 3: Enter two clue Words")
p2_c1 = input('>') # Hints cover up
p2_c2 = input('>') # Hints cover up
clearConsole()
# response = p3_c1 = input('>') # Hints cover up
# response = p3_c2 = input('>') # Hints cover up

# method: how to check clues
Clue_list1 = set([p1_c1.lower(), p1_c2.lower()])
Clue_list2 = set([p2_c1.lower(), p2_c2.lower()])
# Clue_list3 = set([p3_c1, p3_c2])

while True:
    if Clue_list1 == Clue_list2:
        print ("There are no Clues :/")
        break
    else:
        Vaild_Clues = (Clue_list1 | Clue_list2 ) - (Clue_list1 & Clue_list2 )
        print ("Valid Clues are:")
        for x in Vaild_Clues:
            print(x)
    break
    
Score = 0
Cards = 1
print ("Player 1: try to guess the Mystry Word: ")
guess = input(">")
print (guess)
while True:
    if guess.upper() in card1 and guess.upper() == Mystry:
        print ("Correct")
        Score += 1
        Cards -=1
        print ("Score = " ,Score , sep="")
        if Cards <= 0:
            print ("Cards = 0/13")
            playagain()
        else:
            print ("Cards = " + str(Cards) + "/13" , sep="")
        break
    elif guess.upper() == "PASS":
        Cards -=1
        print ("Score = " ,Score , sep="")
        if Cards <= 0:
            print ("Cards = 0/13")
            playagain()
        else:
            print ("Cards = " + str(Cards) + "/13" , sep="")
        break
    else:
        print ("Wrong")
        Cards -=2
        print ("Score = " ,Score , sep="")
        if Cards <= 0:
            print ("Cards = 0/13")
            playagain()
        else:
            print ("Cards = " + str(Cards) + "/13" , sep="")
        break
    
print ("")    
print ("End Of The Demo. Wait For The Full Version :)")

    
    