antwoord = ""


print("Hello You, ik ben Damon Jellema")
print("Wie ben jij?")
naam = input()
print('\n')
print("Hello " + naam)
print('\n')
print("Ik ben een nieuwkomer op het mediacollege Amsterdam")
print("Ik ga een aantal vragen stellen over mij zodat je me beter leert kennen.")
print('\n')
print("Op welke School zat ik voor het mediacollege?:")
print("A.  ClusiusCollege")
print("B.  KennemerCollege Beroepsgericht")
print("C.  De Marel")
antwoord = input().upper()

if antwoord == 'B': 
    print('\n' + "Goed")  
elif antwoord == 'A': 
    print('\n' + "Fout. Het goede antwoord is:" + '\n' + "KennemerCollege Beroepsgericht") 
elif antwoord == 'C':
    print('\n' + "Fout. Het goede antwoord is:" + '\n' + "KennemerCollege Beroepsgericht") 


print('\n' + "Volgende vraag" + '\n' + "Op welke vechtsport zit ik?:")
print("1. Kickboxen")
print("2. shotokan karate")
print("3. Krav Maga")

antwoord = input()
if antwoord == '3': 
    print('\n' + "Goed")  
elif antwoord == '1':
    print('\n' + "Fout. Het goede antwoord is:" + '\n' + "Krav Maga") 
elif antwoord == '2':
    print('\n' + "Fout. Het goede antwoord is:" + '\n' + "Krav Maga")  
print('\n' + "Laatste vraag" + '\n' + "Hoe oud ben ik?:")
print("D. 15")
print("E. 16")
print("F. 18")

antwoord = input().upper()
if antwoord == 'D': 
    print('\n' + "Goed")  
elif antwoord == 'E':
    print('\n' + "Fout. Het goede antwoord is:" + '\n' + "15") 
elif antwoord == 'F':
    print('\n' + "Fout. Het goede antwoord is:" + '\n' + "15") 
print("Einde van de Quiz. Hopelijk weet je nu wat meer van mij.")    