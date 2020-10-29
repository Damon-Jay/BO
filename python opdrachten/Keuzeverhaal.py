import time
import os

os.system("cls")

intro = 1;
vraag1 = 0;
antwoord1 = 0;
vraag2 = 0;
antwoord2 = 0;
vraag3 = 0;
antwoord3 = 0;
vraag4 = 0;
antwoord4 = 0;
vraag5 = 0;
antwoord5 = 0;
vraag6 = 0;
antwoord6 = 0;
vraag7 = 0;
antwoord7 = 0;
vraag8 = 0;
antwoord8 = 0;
vraag9 = 0;
antwoord9 = 0;
vraag10 = 0;
antwoord10 = 0;
vraag11 = 0;
antwoord11 = 0;
vraag12 = 0;
antwoord12 = 0;
vraag13 = 0;
antwoord13 = 0;
vraag14 = 0;
antwoord14 = 0;
vraag15 = 0;
antwoord15 = 0;
vraag16 = 0;
antwoord16 = 0;
vraag17 = 0;
antwoord17 = 0;
vraag18 = 0;
antwoord18 = 0;
vraag19 = 0;
antwoord19 = 0;
vraag20 = 0;
antwoord20 = 0;
vraag21 = 0;
antwoord21 = 0;
vraag22 = 0;
antwoord22 = 0;
vraag23 = 0;
antwoord23 = 0;
vraag24 = 0;
antwoord24 = 0;
vraag25 = 0;
antwoord25 = 0;

while intro == 1:
    print("Je woont in een arm dorpje samen met je Oma, Vader, Moeder en je twee Zussen." + '\n' + "Op een dag krijgen jullie het nieuws dat er extremisten naar jullie dorp komen." + '\n' + "het is heel onveilig")
    vraag1 = 1;
    intro = 0;
    break

while vraag1 == 1:
    print("Ga je vluchten of niet")
    antwoord1 = input("A - Wel of B - Niet : ").upper()
    break

while antwoord1 == 'A':
    vraag2 = 1; 
    break

while antwoord1 == 'B':
    vraag3 = 1;
    break

while vraag3 == 1:
    os.system("cls")
    print('\n' + "Jij en je familie kiezen ervoor om te blijven in jullie dorp. de volgende dag horen jullie schoten. jullie kijken naar buiten en ziet rook in de verte." + "jullie kiezen ervoor om te vluchten. Jullie pakken spullen om te overleven.")
    antwoord3 = input("A - jullie gaat op jullie ezels met spullen er vandoor of B - jullie gaat met een kar met jullie spullen weg : ").upper()
    break
    
while antwoord3 == 'B': 
    print('\n'"Jullie vluchte met de kar maar ze zagen jullie dus jullie werden neergeschoten") 
    break

while antwoord3 == 'A':
    vraag2 = 1;
    break
    
while vraag2 == 1:
    os.system("cls")
    print('\n' + "Jullie vertrekken met jullie ezels richting het noord westen. ze spotten jullie gelukig niet. jullie zijn al 5 uur onderweg.")
    antwoord2 = input("A - Jullie gaan gewoon door of B - jullie gaan even stoppen om te eten en drinken of B : ").upper()
    break

while antwoord2 == 'B': 
    vraag5 = 1; 
    break

while antwoord2 == 'A':
    vraag6 = 1;
    break


while vraag6 == 1:
    os.system("cls")
    print('\n' + "Jullie stoppen niet en gaan gewoon door. na een tijdje zakken jullie ezels in omdat ze honger en dorst hebben.")
    antwoord6 = input("A - jullie gaan stoppen, eten en drinken, de ezels drinken te geven maar geen eten of B - jullie gaan stoppen, eten en drinken, en de ezels krijgen eten en drinken : ").upper()
    break

while antwoord6 == 'B': 
    vraag5 = 1; 
    break

while antwoord6 == 'A':
    vraag7 = 1;
    break

while vraag7 == 1:
    os.system("cls")
    print('\n' + "het is heel laat jullie zijn moe.")
    antwoord7 = input("A - jullie gaan slapen of B - jullie gaan gewoon door : ").upper()
    break

while antwoord7 == 'A': 
    print('\n'"Jullie gingen slapen. later op de avond werden jullie gespot door de extemisten en werden jullie vermoord") 
    break

while antwoord7 == 'B':
    vraag9 = 1;
    break

while vraag5 == 1:
    os.system("cls")
    print('\n' + "Jullie hebben gegeten en gedronken. Ook hebben jullie de ezels eten en drinkengegeven. jullie zien twee paden een gaat naar links en een gaat naar rechts.")
    antwoord5 = input("A - jullie gaan naar links of B - jullie gaan naar rechts : ").upper()
    break

while antwoord5 == 'B': 
    vraag8 = 1; 
    break

while antwoord5 == 'A':
    vraag9 = 1;
    break

while vraag8 == 1:
    os.system("cls")
    print('\n' + "jullie gingen naar rechts. het pad kwam uit in een dichtgegroeid bos.")
    antwoord8 = input("A - gaan jullie terug en nemen het andere pad of B - gaan jullie er doorheen : ").upper()
    break

while antwoord8 == 'B': 
    vraag12 = 1; 
    break

while antwoord8 == 'A':
    vraag9 = 1;
    break   

while vraag9 == 1:
    os.system("cls")
    print('\n' + "Het pad wat jullie namen leed naar de stad Istanboel. de ezels zijn zo uitgeput dat ze niet meer verder kunnen. dus jullie besloten om ze te vermoorden en het vlees voor later mee te nemen. in istanboel kwamen jullie een man tegen. die wilt jullie helpen door een onderdak te geven.")
    antwoord9 = input("A -vertrouw je hem niet en ga weer verder of B - vertrouw je hem wel : ").upper()
    break

while antwoord9 == 'A': 
    vraag12 = 1; 
    break

while antwoord9 == 'B':
    vraag15 = 1;
    break

while vraag12 == 1:
    os.system("cls")
    print('\n' + "jullie gaan istanboel in jullie zien een paar smokkelaars. ook zie je man van daarstraks nog. naar wie ga je.")
    antwoord12 = input("A - ga je naar de smokkelaars of B - of je gaat toch met de man mee : ").upper()
    break

while antwoord12 == 'B': 
    vraag13 = 1; 
    break

while antwoord12 == 'A':
    vraag14 = 1;
    break

while vraag13 == 1:
    os.system("cls")
    print('\n' + "de man zegt tegen de familie over dat die smokkelaars hun kan vervoeren. maar dat ze vandaag vertrekken. de man zij ook dat ze bij hem kunnen blijven voor een tijdje")
    antwoord13 = input("A - ga je naar de smokkelaars of B - of blijft bij de man : ").upper()
    break

while antwoord13 == 'B': 
    vraag15 = 1; 
    break

while antwoord13 == 'A':
    vraag14 = 1;
    break
while vraag14 == 1:
    os.system("cls")
    print('\n' + "Jullie zijn weg gegaan bij de boerderij. jullie zien de smokelaars. dus jullie lopen naar hun toe en vraagt of jullie mee mogen naar een ander land. de smokkelaars zeggen dat jullie mogen kiezen.")
    antwoord14 = input("A - Via de britse smokkelaars of B - via de Bulgaarse smokkelaars : ").upper()
    break

while antwoord14 == 'B': 
    vraag19 = 1; 
    break

while antwoord14 == 'A':
    print('\n'"Jullie gingen met de britse smokkelaars mee naar Oekraïne. Daar zijn jullie afgedropt in een dorpje waar de mensen jullie verder gingen helpen om jullie leven weer te herbouwen")
    break

while vraag15 == 1:
    os.system("cls")
    print('\n' + "hij brengt jullie naar zijn stal en hij geeft jullie eten en drinken. hij gaat samen met jullie eten.")
    antwoord15 = input("A - vertellen jullie NIET de reden waarom jullie zijn gevlucht en vertrekken na het eten of B - vertellen jullie WEL de reden waarom jullie zijn gevlucht : ").upper()
    break

while antwoord15 == 'B': 
    vraag16 = 1; 
    break

while antwoord15 == 'A':
    vraag14 = 1;
    break

while vraag16 == 1:
    os.system("cls")
    print('\n' + "Jullie gaan slapen. Jij wordt wakker door gepraat. je hele familie ligt te slapen. Je hoord de man wat brabbelen. Je weet niet zeker wat je heb gehoord. wat doe je")
    antwoord16 = input("A - Je vertelt tegen je familie dat we weg moeten gaan of B - je gaat weer door slapen : ").upper()
    break

while antwoord16 == 'B': 
    print('\n'"De man was aan de telefoon met een van de extremisten. de volgende dag werden jullie neergeschoten door de extremisten die jullie door de man heeft gevonden")
    break

while antwoord16 == 'A':
    vraag18 = 1;
    break

while vraag18 == 1:
    os.system("cls")
    print('\n' + "Je bent met je familie weg gegaan van de boerderij. maar waar gaan jullie naartoe")
    antwoord18 = input("A - Gaan jullie de stad in of B - Het bos in : ").upper()
    break

while antwoord18 == 'B': 
    print('\n'"Je bent het bos in gegaan alleen de man kon dat zien. jullie zijn achtervolgd door de man en jullie zijn neergeschoten in het bos.") 
    break

while antwoord18 == 'A':
    vraag19 = 1;
    break

while vraag19 == 1:
    os.system("cls")
    print('\n' + "Jullie hebben besloten om met de bulgaarse smokkelaars mee te gaan. De smokkelaars vragen hoe ze vervoerd willen worden")
    antwoord19 = input("A - Met de boot of B - Met een busje : ").upper()
    break

while antwoord19 == 'B': 
    vraag20 = 1;
    break

while antwoord19 == 'A':
    vraag22 = 1;
    break
while vraag19 == 1:
    os.system("cls")
    print('\n' + "Jullie hebben besloten om met de bulgaarse smokkelaars mee te gaan. De smokkelaars vragen hoe ze vervoerd willen worden")
    antwoord19 = input("A - Met een busje naar de kust of B - Met een busje door landen heen : ").upper()
    break

while antwoord19 == 'B': 
    vraag20 = 1;
    break

while antwoord19 == 'A':
    vraag22 = 1;
    break

while vraag22 == 1:
    os.system("cls")
    print('\n' + "Jullie hebben besloten om naar de kust te gaan. De smokkelaars moeten verschillende kanten op")
    antwoord22 = input("A - ga je met de boot of B - verde met het busje").upper()  
    break

while antwoord22 == 'B': 
    vraag20 = 1;
    break

while antwoord22 == 'A':
    vraag23 = 1;
    break

while vraag20 == 1:
    os.system("cls")
    print('\n' + "Jullie hebben besloten om verder te gaan met het busje.Jullie rijden met het busje naar italie. vanaf daar moesten jullie naar andere smokkelaars gaan die twee verschillede kanten op gaan.")
    antwoord20 = input("A - ga je met de een auto naar Nederland of B - Ga je met de boot").upper()
    break

while antwoord20 == 'B': 
    vraag23= 1;
    break

while antwoord20 == 'A':
    print('\n' + "Jullie hebben besloten om naar Nederland te gaan. Jullie reden Naar nederland. toen jullie daar aankwamen werden jullie opgevangen. jullie vroegen een asielvergunning aan. jullie haalden de inburgeringstest en mochten daarom in Nederland blijven.")
    break
 
while vraag23 == 1:
    os.system("cls")
    print('\n' + "Jullie hebben besloten om naar de kust te gaan en dan met de boot vervoerd te worden. alleen de smokkelaars moeten naar twee verschillende landen. met welke ga je mee")
    antwoord23 = input("A - ga je naar Nederland of B - je gaat naar Tunesië: ").upper()
    break

while antwoord23 == 'B': 
    print('\n' + "Jullie hebben besloten om naar Tunesië te gaan. Jullie vaarde daar nartoe alleen de de golfen waren te hoog en jullie zijn daardoor verdronken")
    break

while antwoord23 == 'A':
    print('\n' + "Jullie hebben besloten om naar Nederland te gaan. Jullie vaarde succesvol Naar nederland. toen jullie daar aankwamen werden jullie opgevangen. jullie vroegen een asielvergunning aan. jullie haalden de inburgeringstest en mochten daarom in Nederland blijven.")
    break