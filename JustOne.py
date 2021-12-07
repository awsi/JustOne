

print("Hallo! Willkommen bei JustOne! Möchten Sie erst die Regeln erfahren? (ja/nein)")
response = input('>')
if response.lower() == 'ja':
    print ('"REGELN"')
    print ('_ _ _ _ _ _ _ _ _ _ _ _ _')
    print ('Bitte geben Sie die Anzahl der Spieler ein:')
else:
    print ("Bitte geben Sie die Anzahl der Spieler ein:")
Number_Of_Players = int(input('>'))
Wörter = ["Apfel", "Hund", "Eis", "Zimmer", "Club"]
print ("Spieler 1: Wählen Sie ein Wort von 1 bis 5 und drehen Sie sich bitte um:)")
response = input('>')
print ("Das gewählte Word ist:")

while True:
    if response == "1":
        print (Wörter[0])
        break
    elif response == "2":
        print (Wörter[1])
        break
    elif response == "3":
        print (Wörter[2])
        break
    elif response == "4":
        print (Wörter[3])
        break
    elif response == "5":
        print (Wörter[4])
        break
    else:
        print("Bitte geben Sie eine Zahl von 1 bis 5 ein") #verwenden einen Loop
        break
    
print ("Spieler 3: Augen zu :)")
print ("Spieler 2: Geben Sie zwei hinweise Wörter ein:")
response = s1_h1 = input('>')
response = s1_h2 = input('>')
print ("Spieler 2: Augen zu :)")
print ("Spieler 3: Geben Sie zwei hinweise Wörter ein:")
response = s2_h1 = input('>')
response = s2_h2 = input('>')

print ("Die Hinweise werden überprüft...")

# eine Idea zur Überprüfung der Hinweise (ist aber immer noch an der Bearbeitung)
"""Hinweise = [s1_h1, s1_h2, s2_h1, s2_h2] 
for x in Hinweise:
    if s1_h1.lower() == s2_h1.lower():
        Hinweise.pop(0)
        Hinweise.pop(1)
        print (s1_h2,s2_h2)
        print (Hinweise)
        print ('__________')
        print (x)"""