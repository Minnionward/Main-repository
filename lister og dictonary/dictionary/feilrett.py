# -*- coding: utf-8 -*-
def centner(x):
        return x * float(0.01)

def newton(x):
        return x * float(9.89)
def karat(x):
        
        return x * int(5000)

while True:


#Spør bruker hvilken enhet de vil konvertere.    

    verdi = int(input("Hva vil du konvertere? Centner (c eller C), Newton (n eller N) eller Karat (k eller K)."))


    if verdi == "c" or verdi == "C":

        v = float(input("Hvor mange kg vil du konvertere?"))

        print(centner(v))       

 

    elif verdi == "n" or verdi == "N":

        v = float(input("Hvor mange kg vil du konvertere?"))

        print(newton(v))      

    elif verdi == "k" or verdi == "K":

        v = int(input("Hvor mange kg vil du konvertere?"))

        print(karat(v))        

    

    else:

        print("Du har ikke valgt en gyldig enhet!")

    

#Gir brukeren mulighet til å kjøre en ny konvertering ved å skrive nei.

#Skriver brukeren ja, vil programmet avsluttes (break)

    for avslutning in range(1):

        avslutt = input("Hvis du vil avslutte programmet - skriv ja. Om ikke -s kriv nei ")



    if avslutt == "ja":

        

        break

    if avslutt == "nei":

        continue