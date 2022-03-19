
import os
from click import style
import requests
import random
import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)
import warnings
warnings.simplefilter("ignore", UserWarning)
from tabulate import tabulate
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import spacy
nlp = spacy.load('en_core_web_md')

#https://www.delftstack.com/de/howto/python/python-clear-console/
def clearConsole():
    command = 'clear' if os.name not in ('nt', 'dos') else 'cls'  # If Machine is running on Windows, use cls
    os.system(command)
    
clearConsole()
playagain = "yes"
while playagain == "yes":
    print(Fore.YELLOW + "Hello! Welcome to JustOne! Would you like to know the rules first? (yes/no)")
    response = input('>')
    if response.lower() == "yes":
        clearConsole()
        print (Fore.RED+Back.WHITE+Style.BRIGHT+ "*********************************************** ~--( Rules )--~ ***********************************************")
        print (Fore.CYAN+
            "* The game works like this: Randomly choose a player to be the first active player (player 1).\n"
            "The active player chooses a number between 1 - 5 to generate the mystery word for a round.\n"
            "The other player can see the mystery word now and has to provide two clues.\n"
            "Without communicating with player(1) and without showing clues, player(2) enters two clues.\n"
            "Each clue must be composed of a single word.\n"
            "Once Player(2) has entered their clues, CPU will provide two clues.\n"
            "Note: All identical or invalid clues will be cancelled.\n"
            "Once the identical or invalid clues have been cancelled, ask the active player to open their eyes\n"
            "and try to guess the Mystery word with the help of the remaining clues. To do this, they're allowed ONLY ONE GUESS.\n"
            "\n"
            "* Results: \n"
            "- "+ Back.GREEN + "Success:" + Back.RESET + " If the active player correctly guesses the Mystery word:\n"
            "   -> Plus one point on the point score and the round score starts with the next card.\n"
            "- "+Back.RED + "Failure:" + Back.RESET + " If the active player makes a wrong guess:\n"
            "   -> No points added to score plus one penalty lap for the round score.\n"
            "- "+Back.WHITE + "Skip:" + Back.RESET + " If the active player chooses not to answer and skips their turn by entering "+ Back.YELLOW +"'PASS'" + Back.RESET + ":\n"
            "   -> No points added to score, but no penalty lap for the round score\n"
            "- End of the Turn: The player to the left of the active player becomes the new active player. A new turn begins.\n"
            "- End of the Game: The game ends when all 13 cards of a round has been played.\n"
            "- Your goal is to score as many points as possible at the end of the game.\n"
            "- The higher the better.")
        print (Fore.RED+Back.WHITE+Style.BRIGHT+ "***************************************************************************************************************")
        print ("")

    else:
        clearConsole()
        
    print (Fore.YELLOW + "-> The game is designed for 2 people make sure who starts to guess then press anykey to start the game <-")
    input(">")
    clearConsole()
    cards = ['WATER', 'FISH', 'BIRD', 'CAR', 'CHAIR', 'MUG', 'CHEESE', 'CAMERA', 'CAKE', 'CLOCK', 'FIRE', 'EARTH', 'GARDEN', 'BOAT', 'MOON', 'MOUTH', 'APPLE', 'GUITAR', 'AIR', 'SKY', 'HORSE', 'BOOK', 'MUSIC', 'RAIN', 'ANIMAL', 'CAPTAIN', 'FROG', 'MONKEY', 'SHIELD', 'BAG', 'KING', 'GAME', 'SNOW', 'BEE', 'SCHOOL', 'LOVE', 'DOLLAR', 'DOCTOR', 'INSECT', 'POISON', 'GOLD', 'PAIN', 'CONTINENT', 'RADIO', 'PHONE', 'METAL', 'DESK', 'SCIENCE', 'GUN', 'SPACE', 'FILM', 'LANGUAGE', 'BED', 'COFFEE', 'EYE', 'WINE', 'WOOD', 'BRIDGE', 'BALL', 'SQUIRREL', 'PAPER', 'CHOCOLATE', 'DOOR', 'SUN', 'WEEK', 'PARTY', 'MOTHER', 'SUGAR', 'SALT', 'NOSE', 'RELIGION', 'DESERT']
    
    Score = 0
    Cards = 13
    Rounds = 0
    while Cards > 0:
        Rounds += 1
        print(Fore.RED+Back.WHITE+Style.BRIGHT + "*********************************************** ~--( Round:", f'\033[36;47m{Rounds}\033[0m', Fore.RED+Back.WHITE+Style.BRIGHT + " )--~ ***********************************************", sep="")
        print (Fore.BLUE + "Active Player: " + Fore.YELLOW + "enter a number between 1 and 5 to choose the mystry word and turn around :)")
    
        Mystry = []
        x = ["1", "2", "3", "4", "5"]
        while True:
            response = input(Fore.BLUE + '>')
            if response not in x:
                clearConsole()
                print(Fore.RED+Back.WHITE+Style.BRIGHT + "*********************************************** ~--( Round:", f'\033[36;47m{Rounds}\033[0m', Fore.RED+Back.WHITE+Style.BRIGHT + " )--~ ***********************************************", sep="")
                print (Fore.BLUE + "Active Player: " + Fore.YELLOW + "enter a number between 1 and 5 to choose the mystry word and turn around :)")
            else:
                Mystry = random.choice(cards)
                ind = cards.index(Mystry)
                cards.pop(ind)
                break
        clearConsole()
        print (Fore.YELLOW + "The mystery word is:", "\033[35m" + Mystry + "\033[0m")
        print (Fore.GREEN + "Player(2): " + Fore.YELLOW + "Enter two clues:")
        p1_c1 = input(Fore.GREEN + '>')
        p1_c2 = input(Fore.GREEN + '>')
        clearConsole()
    
        api_url = "http://api.conceptnet.io/"
        lang = "query?start=/c/en/"
        limit = "&limit=1000"

        # Mystry = requests.get('http://api.conceptnet.io/query?start=/c/en/elephant&limit=40').json()
        Mystry_concept = requests.get(api_url + lang + Mystry.lower() + limit).json()

        Mystry_concept.keys()
    
        edges = Mystry_concept["edges"]
        list_of_relations = []
        for e in edges:
            if (e["rel"]["label"] == "RelatedTo" ) and (e['end']['language'] == "en"):
      
                temp_word = e['end']['label']
                if len(temp_word.split()) == 1 and (Mystry.lower() not in temp_word):
                    list_of_relations.append(e['end']['label'])
                    
        def get_wordnet_pos(word):
                """Map POS tag to first character lemmatize() accepts"""
                tag = nltk.pos_tag([word])[0][1][0].upper()
                tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

                return tag_dict.get(tag, wordnet.NOUN)
        lmtzr = WordNetLemmatizer()
        lemmatized = set([lmtzr.lemmatize(w, get_wordnet_pos(w)) for w in list_of_relations])
        Mystry_nlp = nlp(Mystry)
        
        similarity = [(w, Mystry_nlp.similarity(nlp(w))) for w in lemmatized]
        similarity.sort(key=lambda x: x[1], reverse=True)

        LemaAndSima = []
        for w, value in similarity:
            if 0.9 > value > 0.4:
                LemaAndSima.append(w)
                #print(f"{Mystry} - {w}", value)
     
        conceptnet_clues = random.sample(LemaAndSima, 2)
        
        Clue_list1 = set([p1_c1.lower().strip(), p1_c2.lower().strip()])
        Clue_list2 = set(conceptnet_clues)
        print("-----------------")
        print("Number of Words:", len(list_of_relations))
        print("Relatedterms RAW:", (list_of_relations))
        print("-----------------")
        print("Number of Words:", len(lemmatized))
        print ("lemmatized:" , list(lemmatized))
        print("-----------------")
        print ("similarity (all values):" , similarity)
        print("-----------------")
        print("Number of Words:", len(LemaAndSima))
        print ("LemaAndSima ( 0.9 > value > 0.4 ):" , LemaAndSima)
        print("-----------------")
        print("CPU clues:", conceptnet_clues)
        print("-----------------")
        print("User's clues:", list(Clue_list1))
        print("-----------------")

        while True:
            if Clue_list1 == Clue_list2:
                print (Fore.YELLOW + "all clues are unvalid :/")
                break
            elif (p1_c1.lower().strip() in Mystry.lower()) and (p1_c2.lower().strip() in Mystry.lower()):
                print(Fore.YELLOW + "Valid clues are:")
                for clue in conceptnet_clues:
                    print("\033[32m" + clue + "\033[0m")
                break
            elif (p1_c1.lower().strip()) in Mystry.lower():
                print(Fore.YELLOW + "Valid clues are:") 
                conceptnet_clues += [p1_c2.lower().strip()]
                for clue in conceptnet_clues:
                    print("\033[32m" + clue + "\033[0m")
                break
            elif (p1_c2.lower().strip()) in Mystry.lower():
                print(Fore.YELLOW + "Valid clues are:") 
                conceptnet_clues += [p1_c1.lower().strip()]
                for clue in conceptnet_clues:
                    print("\033[32m" + clue + "\033[0m")
                break
            else:
                Vaild_Clues = (Clue_list1 | Clue_list2 ) - (Clue_list1 & Clue_list2) #falls CPU & User gleiche hinweise eingeben werden sie weggenommen
                print (Fore.YELLOW + "Valid clues are:")
                for x in Vaild_Clues:
                    print("\033[32m" + x + "\033[0m")
                break

        print (Fore.BLUE + "Active Player: " + Fore.YELLOW + "Try to guess the mystry word/or enter 'Pass' to skip the round: ")
        guess = input(Fore.BLUE + ">")
        #print ("----------------- + ----------------- + ----------------- + ----------------- + -----------------")
        clearConsole()
        print (Fore.YELLOW + "The mystry word is: " + "\033[35m" + Mystry + "\033[0m")
        while True:
            if guess.upper() == Mystry:
                print (Fore.GREEN + "Correct")
                Score += 1
                Cards -=1
                print (Fore.YELLOW + "Score = " ,f'\033[32m{Score}\033[0m' , sep="")
                if Cards <= 0:
                    print (Fore.YELLOW + "Cards = 0/13")
                    #print ("----------------- + ----------------- + ----------------- + ----------------- + -----------------")
                    break
                else:
                    print (Fore.YELLOW + "Cards = " + str(Cards) + "/13" , sep="")
                    #print ("----------------- + ----------------- + ----------------- + ----------------- + -----------------")
                    break
            elif guess.upper() == "PASS":
                Cards -=1
                print (Fore.YELLOW + "Score = " ,f'\033[32m{Score}\033[0m' , sep="")
                if Cards <= 0:
                    print (Fore.YELLOW + "Cards = 0/13")
                    #print ("----------------- + ----------------- + ----------------- + ----------------- + -----------------")
                    break
                else:
                    print (Fore.YELLOW + "Cards = " + str(Cards) + "/13" , sep="")
                    #print ("----------------- + ----------------- + ----------------- + ----------------- + -----------------")
                    break
            else:
                print (Fore.RED + "Wrong")
                Cards -=2
                print (Fore.YELLOW + "Score = " ,f'\033[32m{Score}\033[0m' , sep="")
                if Cards <= 0:
                    print (Fore.YELLOW + "Cards = 0/13")
                    #print ("----------------- + ----------------- + ----------------- + ----------------- + -----------------")
                    break
                else:
                    print (Fore.YELLOW + "Cards = " + str(Cards) + "/13" , sep="")
                    #print ("----------------- + ----------------- + ----------------- + ----------------- + -----------------")
                    break        
        if Cards <= 0:
            print("")
            if Score <= 3:
                table = [["\033[31;47m" + "Score" + "\033[0m", "\033[31;47m" + "Interpretation" + "\033[0m"], ["13", "Perfect score! Can you do it again?!"], ["12", "Incredible! Your friends must be impressed!"], ["11", "Awesome! That's a score worth celebrating!"], ["9-10", "Wow, not bad at all!"], ["7-8", "You're in the average. Can you do better?"], ["4-6", "That's a good start. Try again!"], [("\033[31m" + "0-3" + "\033[0m"), ("\033[31m" + "Try again, and again, and again."+ "\033[0m")]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            elif 4 >= Score <= 6:
                table = [["\033[31;47m" + "Score" + "\033[0m", "\033[31;47m" + "Interpretation" + "\033[0m"], ["13", "Perfect score! Can you do it again?!"], ["12", "Incredible! Your friends must be impressed!"], ["11", "Awesome! That's a score worth celebrating!"], ["9-10", "Wow, not bad at all!"], ["7-8", "You're in the average. Can you do better?"], ["\033[38;5;208m"+"4-6"+"\033[0m", "\033[38;5;208m"+"That's a good start. Try again!"+"\033[0m"], ["0-3", "Try again, and again, and again."]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            elif 7 >= Score <= 8:
                table = [["\033[31;47m" + "Score" + "\033[0m", "\033[31;47m" + "Interpretation" + "\033[0m"], ["13", "Perfect score! Can you do it again?!"], ["12", "Incredible! Your friends must be impressed!"], ["11", "Awesome! That's a score worth celebrating!"], ["9-10", "Wow, not bad at all!"], ["\033[38;5;214m"+"7-8"+"\033[0m", "\033[38;5;214m"+"You're in the average. Can you do better?"+"\033[0m"], ["4-6", "That's a good start. Try again!"], ["0-3", "Try again, and again, and again."]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            elif 9 >= Score <= 10:
                table = [["\033[31;47m" + "Score" + "\033[0m", "\033[31;47m" + "Interpretation" + "\033[0m"], ["13", "Perfect score! Can you do it again?!"], ["12", "Incredible! Your friends must be impressed!"], ["11", "Awesome! That's a score worth celebrating!"], ["\033[38;5;226m"+"9-10"+"\033[0m", "\033[38;5;226m"+"Wow, not bad at all!"+"\033[0m"], ["7-8", "You're in the average. Can you do better?"], ["4-6", "That's a good start. Try again!"], ["0-3", "Try again, and again, and again."]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            elif Score == 11:
                table = [["\033[31;47m" + "Score" + "\033[0m", "\033[31;47m" + "Interpretation" + "\033[0m"], ["13", "Perfect score! Can you do it again?!"], ["12", "Incredible! Your friends must be impressed!"], ["\033[38;5;191m"+"11"+"\033[0m", "\033[38;5;191m"+"Awesome! That's a score worth celebrating!"+"\033[0m"], ["9-10", "Wow, not bad at all!"], ["7-8", "You're in the average. Can you do better?"], ["4-6", "That's a good start. Try again!"], ["0-3", "Try again, and again, and again."]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            elif Score == 12:
                table = [["\033[31;47m" + "Score" + "\033[0m", "\033[31;47m" + "Interpretation" + "\033[0m"], ["13", "Perfect score! Can you do it again?!"], ["\033[38;5;156m"+"12"+"\033[0m","\033[38;5;156"+ "Incredible! Your friends must be impressed!"+"\033[0m"], ["11", "Awesome! That's a score worth celebrating!"], ["9-10", "Wow, not bad at all!"], ["7-8", "You're in the average. Can you do better?"], ["4-6", "That's a good start. Try again!"], ["0-3", "Try again, and again, and again."]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            else:
                table = [["\033[31;47m" + "Score" + "\033[0m", "\033[31;47m" + "Interpretation" + "\033[0m"], ["\033[38;5;46m"+"13"+ "\033[0m", "\033[38;5;46m"+"Perfect score! Can you do it again?!"+ "\033[0m"], ["12", "Incredible! Your friends must be impressed!"], ["11", "Awesome! That's a score worth celebrating!"], ["9-10", "Wow, not bad at all!"], ["7-8", "You're in the average. Can you do better?"], ["4-6", "That's a good start. Try again!"], ["0-3", "Try again, and again, and again."]]
                print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    print("")
    print("")
    print(Fore.YELLOW + "End of the Game.")
    print("")
    print(Fore.YELLOW + "enter 'yes' to play again or anykey to exit.")
    playagain = input(">")
    if playagain != "yes":
        print("")
        print (Fore.YELLOW + "Ok, Bye-bye! :)")
    else:
        clearConsole()
