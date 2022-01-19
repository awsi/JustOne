
import os
import requests
import random
from tabulate import tabulate

#https://www.delftstack.com/de/howto/python/python-clear-console/
def clearConsole():
    command = 'clear' if os.name not in ('nt', 'dos') else 'cls'  # If Machine is running on Windows, use cls
    os.system(command)
    
playagain = "yes"
while playagain == "yes":

    print("Hello! Welcome to JustOne! Would you like to know the rules first? (yes/no)")
    response = input('>')
    if response.lower() == "yes":
        #print ('"RULES"')  
        print ("* The game works like this: Randomly choose a player to be the first active player (player 1).\n"
            "The active player chooses a number between 1 - 5 to generate the mystery word for a round.\n"
            "The other player can see the mystery word now and has to provide two clues.\n"
            "Without communicating with player(1) and without showing clues, player(2) enters two clues.\n"
            "Each clue must be composed of a single word.\n"
            "Once Player(2) has entered their clues, CPU will provide two clues.\n"
            "Note: All identical or invalid clues will be cancelled.\n"
            "Once the identical or invalid clues have been cancelled, ask the active player to open their eyes\n"
            "and try to guess the Mystery word with the help of the remaining clues. To do this, they're allowed ONLY ONE GUESS.\n"
            "* Results:\n"
            "- Success: If the active player correctly guesses the Mystery word:\n"
            "Plus one point on the point score and the round score starts with the next card.\n"
            "- Failure: If the active player makes a wrong guess:\n"
            "No points added to score plus one penalty lap for the round score.\n"
            "- Skip: If the active player chooses not to answer and skips their turn by entering 'PASS':\n"
            "No points added to score, but no penalty lap for the round score\n"
            "- End of the Turn: The player to the left of the active player becomes the new active player. A new turn begins.\n"
            "- End of the Game: The game ends when all 13 cards of a round has been played.")
        print("")
        print ('Please enter the number of players: (ONLY THREE PLAYERS) ')
    else:
        print ("Please enter the number of players: (ONLY THREE PLAYERS) ") # (Demo: 3 Players , Full Game: up to 7 Players)

    Number_Of_Players = input('>')
    clearConsole()
#while True:
    if Number_Of_Players == "3":
        print("")
    else:
        print("")
        #clearConsole()
        #sys.exit(":( Please restart the Game and enter number 3")

    cards = ["FLOUR", "MONKEY", "DOLLAR", "LOVE", "POISON", "GUN", "INSECT", "PYRAMID", "DOG", "FROG", "BEE", "FIRE", "RELIGION", "SUN"]    
    Score = 0
    Cards = 13       
    while Cards > 0:
        print ("Aktive Player: enter a number between 1 and 5 to choose the mystry word and turn around :)")
    
        Mystry = []
        x = ["1", "2", "3", "4", "5"]
        while True:
            response = input('>')
            if response not in x:
                print ("Aktive Player: enter a number between 1 and 5 to choose the Mystry word and turn around :)")
            else:
                Mystry = random.choice(cards)
                ind = cards.index(Mystry)
                cards.pop(ind)
                break
        
        print ("The mystery word is:", Mystry)
        print ("Player(2): Enter two clues:")
        p1_c1 = input('>') # Hints cover up
        p1_c2 = input('>') # Hints cover up
        clearConsole()
    
        api_url = "http://api.conceptnet.io/"
        lang = "query?start=/c/en/"
        limit = "&limit=40"

        # Mystry = requests.get('http://api.conceptnet.io/query?start=/c/en/elephant&limit=40').json()
        Mystry_concept = requests.get(api_url + lang + Mystry.lower() + limit).json()

        Mystry_concept.keys()
    
        edges = Mystry_concept["edges"]
        list_of_relations = []
        for e in edges:
            if e["rel"]["label"] == "RelatedTo":
      
                temp_word = e['end']['label']
                if len(temp_word.split()) == 1 and (Mystry not in temp_word):
                    list_of_relations.append(e['end']['label'])
        conceptnet_clues = random.sample(list_of_relations, 2)
    #clearConsole()
# p3_c1 = input('>') # Hints cover up
# p3_c2 = input('>') # Hints cover up

# method: how to check clues
        Clue_list1 = set([p1_c1.lower().strip(), p1_c2.lower().strip()])
        Clue_list2 = set(conceptnet_clues)
        print("-----------------")
        print ("ReletedTerms words:" , list_of_relations)
        print("ConceptNet clues:", conceptnet_clues)
        print("User's clues:", list(Clue_list1))
#Clue_list3 = set([p3_c1.lower(), p3_c2.lower()])
# Clue_list3 = set([p3_c1, p3_c2])

        while True:
            if Clue_list1 == Clue_list2:
                print ("all clues are unvalid :/")
                break
            elif (p1_c1.lower().strip() in Mystry.lower()) and (p1_c2.lower().strip() in Mystry.lower()):
                print("Valid clues are:")
                for clue in conceptnet_clues:
                    print(clue)
                break
            elif (p1_c1.lower().strip()) in Mystry.lower():
                print("Valid clues are:") 
                conceptnet_clues += [p1_c2.lower().strip()]
                for clue in conceptnet_clues:
                    print(clue)
                break
            elif (p1_c2.lower().strip()) in Mystry.lower():
                print("Valid clues are:") 
                conceptnet_clues += [p1_c1.lower().strip()]
                for clue in conceptnet_clues:
                    print(clue)
                break
            else:
                Vaild_Clues = (Clue_list1 | Clue_list2 ) - (Clue_list1 & Clue_list2)
                print("Valid clues:", list(Vaild_Clues))
                print ("Valid clues are:")
                for x in Vaild_Clues:
                    print(x)
                break
    #print(p1_c1)
        print ("Aktive Player: Try to guess the mystry word: ")
        guess = input(">")
        print ("-----------------")
        print ("The mystry word is:",Mystry)
        while True:
            if guess.upper() == Mystry:
                print ("Correct")
                Score += 1
                Cards -=1
                print ("Score = " ,Score , sep="")
                if Cards <= 0:
                    print ("Cards = 0/13")
                    print ("-----------------")
                    break
                else:
                    print ("Cards = " + str(Cards) + "/13" , sep="")
                    print ("-----------------")
                    break
            elif guess.upper() == "PASS":
                Cards -=1
                print ("Score = " ,Score , sep="")
                if Cards <= 0:
                    print ("Cards = 0/13")
                    print ("-----------------")
                    break
                else:
                    print ("Cards = " + str(Cards) + "/13" , sep="")
                    print ("-----------------")
                    break
            else:
                print ("Wrong")
                Cards -=2
                print ("Score = " ,Score , sep="")
                if Cards <= 0:
                    print ("Cards = 0/13")
                    print ("-----------------")
                    break
                else:
                    print ("Cards = " + str(Cards) + "/13" , sep="")
                    print ("-----------------")
                    break        
        if Cards <= 0:
            table = [["Score", "Interpretation"], ["13", "Perfect score! Can you do it again?!"], ["12", "Incredible! Your friends must be impressed!"], ["11", "Awesome! That's a score worth celebrating!"], ["9-10", "Wow, not bad at all!"], ["7-8", "You're in the average. Can you do better?"], ["4-6", "That's a good start. Try again!"], ["0-3", "Try again, and again, and again."]]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    print("")
    print("")
    print("End of the Game.")
    print("")
    print("enter 'yes' to play again or anykey to exit.")
    playagain = input(">")
    if playagain != "yes":
        print("")
        print ("Ok, Bye-bye! :)")
    else:
        print("")
        
        

"""if Cards <= 0:
            if Score == 13:
                print("Perfect score! Can you do it again?!")
            elif Score == 12:
                print("Incredible! Your friends must be impressed!")
            elif Score == 11:
                print("Awesome! That's a score worth celebrating!")
            elif Score == (9 or 10):
                print("Wow, not bad at all!")
            elif Score == (7 or 8):
                print("You're in the average. Can you do better?")
            elif Score == (4 or 5 or 6):
                print("That's a good start. Try again!")
            else:
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        
    
    table13 = [["Successful Cards", "Score"], [Score, "Perfect score! Can you do it again?!"]]
            table12 = [["Successful Cards", "Score"], [Score, "Incredible! Your friends must be impressed!"]]
            table11 = [["Successful Cards", "Score"], [Score, "Awesome! That's a score worth celebrating!"]]
            table10 = [["Successful Cards", "Score"], [Score, "Wow, not bad at all!"]]
            table8 = [["Successful Cards", "Score"], [Score, "You're in the average. Can you do better?"]]
            table6 = [["Successful Cards", "Score"], [Score, "That's a good start. Try again!"]]
            table3 = [["Successful Cards", "Score"], [Score, "Try again, and again, and again."]]
            if Score == 13:
                print(tabulate(table13, headers='firstrow', tablefmt='fancy_grid'))
            elif Score == 12:
                print(tabulate(table12, headers='firstrow', tablefmt='fancy_grid'))
            elif Score == 11:
                print(tabulate(table11, headers='firstrow', tablefmt='fancy_grid'))
            elif Score == (9 or 10):
                print(tabulate(table10, headers='firstrow', tablefmt='fancy_grid'))
            elif Score == (7 or 8):
                print(tabulate(table8, headers='firstrow', tablefmt='fancy_grid'))
            elif Score == (4 or 5 or 6):
                print(tabulate(table6, headers='firstrow', tablefmt='fancy_grid'))
            else:
                print(tabulate(table3, headers='firstrow', tablefmt='fancy_grid'))"""""