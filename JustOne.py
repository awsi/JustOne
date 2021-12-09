

print("Hello! Welcome to JustOne! Would you like to know the rules first? (Yes/No)")
response = input('>')
if response.lower() == 'yes':
    print ('"RULES"') 
    print ('_ _ _ _ _ _ _ _ _ _ _ _ _')
    print ('Please enter the number of players: ')
else:
    print ("Please enter the number of players: ") # (Demo: 3 Players , Full Game: up to 7 Players)
Number_Of_Players = int(input('>'))
Words = ["Apple", "Dog", "Ice", "Room", "Club"] # Karte zeigen
print ("Player 1: Choose a word between 1 and 5 and please turn around :)")
response = input('>')
print ("The Mystery word is: ")

while True:
    if response == "1":
        print (Words[0])
        break
    elif response == "2":
        print (Words[1])
        break
    elif response == "3":
        print (Words[2])
        break
    elif response == "4":
        print (Words[3])
        break
    elif response == "5":
        print (Words[4])
        break
    else:
        print("Please enter a number between 1 and 5") #use a loop to make the aktive players enter a number again
        break
    
print ("Player 3: Eyes closed :)")
print ("Player 2: ُEnter two clue Words:")
response = p1_c1 = input('>') # Hints cover up
response = p1_c2 = input('>') # Hints cover up
print ("Plazer 2: Eyes closed :)")
print ("Plazer 3: Enter two clue Words")
response = p2_c1 = input('>') # Hints cover up
response = p2_c2 = input('>') # Hints cover up

# print ("The clue words are checked...")

# a mrthod how to chekck clue words:
Clue_Words = [p1_c1, p1_c2, p2_c1, p2_c2] 
for x in Clue_Words:
    if p1_c1.lower() == p2_c1.lower():
        Clue_Words.pop(0)
        # Hinweise.pop(1)
        print (p1_c2)
        print (p2_c2)
        break
        # print (Hinweise)
        # print ('__________')
        # print (x)