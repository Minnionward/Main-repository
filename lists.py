brukernavn = []
passord = []

def legg_til_bruker():
    nytt_brukernavn = input("skriv in brukernavn")
    nytt_passord = input("skriv inn nytt passord")
    brukernavn.append(nytt_brukernavn)
    passord.append(passord)
    print(" bruker er lagt til")

def logg_inn():
    nBruker = input ("skriv inn ditt brukernavn")
    Npass = input (" skriv inn ditt passord")

    if nBruker in brukernavn and Npass == passord[brukernavn.index(nBruker)]:
        print("du er logget in")
    else: print("feil passord eller brukernavn")


def hovedprogram():
    while True:
        print("Velg en handling:")
        print("1. Legg til bruker")
        print("2. Logg inn")
        print("3. Avslutt")
        
        valg = input("skriv inn valg 1/2/3: ")
        
        if valg == '1':
            legg_til_bruker()
        elif valg == '2':
            logg_inn()
        elif valg == '3':
            break
        else:
            print("ugyldig valg")



        

        


    