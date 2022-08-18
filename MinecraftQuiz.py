import time
import msvcrt

Score=0
Answer_1 = 0
Answer_2 = 0
Answer_3 = 0
Answer_4 = 0
Answer_5 = 0

print("##Minecraft Quizspiel in Python##")
print("Gemacht von Michael")
time.sleep(2)
print("")
##Frage1


print("Frage 1: ")
print("Seit welchem Jahr gibt es das Spiel -Minecraft-?")
time.sleep(2)
print(" A: 2009  B: 2012  C: 2004")
print("")

while Answer_1 != "A" and Answer_1 != "B" and Answer_1 != "C":
    Answer_1 =(input("Antwort eingeben: "))

print("")

if Answer_1 == "A":
    print("Das ist richtig! Minecraft wird seit 2009 entwickelt, und kriegt immer neue Updates.")
    Score += 50
    print("Dein Punktestand: " + str(Score))
elif Answer_1 == "B" or "C":
    print("Das ist leider falsch.")
    time.sleep(1)
    print("Richtige Antwort: A")
    print("Minecraft wird seit 2009 entwickelt und kriegt immer neue Updates.")
    time.sleep(1)
    print("Dein Punktestand: "+ str(Score))
else:
    print("Nanu? Wie geht denn das?")
    print(Answer_1)

time.sleep(5)

print("")

##Frage2
print("Frage 2: ")
print("Wie heißt die Ausrüstung, mit der man in der Luft gleiten kann?")
time.sleep(2)
print(" A: Flügel  B: Gleiter  C: Elytren  D: Insektending")
print("")

while Answer_2 != "A" and Answer_2 != "B" and Answer_2 != "C" and Answer_2 != "D":
    Answer_2 =(input("Antwort eingeben: "))

print("")

if Answer_2 == "C":
    print("Das ist richtig!")
    Score= Score+50
    print("Dein Punktestand: " + str(Score))
elif Answer_2 == "A" or "B" or "D":
    print("Das ist leider falsch.")
    time.sleep(1)
    print("Richtige Antwort: C",end ="")
    print(", sie heißen Elytren.")
    time.sleep(1)
    print("Dein Punktestand: "+ str(Score))
else:
    print("Nanu? Wie geht denn das?")
    print(Answer_2)
time.sleep(5)
#frage3
print("")
print("Frage 3: ")
print("Wieviele Herzen hat ein Spieler?")
time.sleep(2)
print(" A: 20  B: 5  C: 40  D: 10")
print("")

while Answer_3 != "A" and Answer_3 != "B" and Answer_3 != "C" and Answer_3 != "D":
    Answer_3 =(input("Antwort eingeben: "))

print("")

if Answer_3 == "D":
    print("Das ist richtig! Ein Spieler hat 10 Herzen, die in 20 Schadenspunkte unterteilt sind.")
    Score +=50
    print("Dein Punktestand: "+ str(Score))
elif Answer_3 == "A" or "B" or "C":
    print("Das ist falsch! Richtige antwort: D, ein Spieler hat 10 Herzen, in 20 Schadenspunkte unterteilt.")
else:
    print("Nanu? Wie geht denn das?")
    print(Answer_3)

time.sleep(5)
print("")

#frage4
print(" ")
print("Frage 4: ")
print("Was ist ein -Creeper-?")
time.sleep(2)
print(" A: Ein Monster  B: Eine Pflanze  C: Ein Haustier  D: Ein Terrorist")
print(" ")

print("")

while Answer_4 != "A" and Answer_4 != "B" and Answer_4 != "C" and Answer_4 != "D":
    Answer_4 =(input("Antwort eingeben: "))

print("")

if Answer_4 == "A" or "D":
    print("Das ist richtig! Ein Creeper ist ein Monster, das sich selber in die Luft sprengt.")
    Score += 50
    print("Dein Punktestand: " + str(Score))
elif Answer_4 == "B" or "C" :
    print("Das ist falsch! Richtige antwort: A oder D, ein Creeper ist ein Monster, das sich selber in die Luft sprengt.")
else:
    print("Nanu? Wie geht denn das?")
    print(Answer_4)

time.sleep(5)
print("")

print("Vielen dank fürs Spielen!")
print("Ihre Gesamtpunktzahl ist: "+ str(Score)+"!")

CRK = msvcrt.getch()
CRK = input()
print(CRK)


