bruker = "Arthur"
passord = "secret"

bruker_in = input("skriv in brukernavn")
passord_in =input("skriv in passord")
 
if (bruker == bruker_in) and (passord == passord_in):
    print("login korrekt")
else:
    print ("feil passord eller brukernavn")
