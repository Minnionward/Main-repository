from pymongo import MongoClient
import pymongo

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "Arthur"
COLLECTION_ANSATTE = "ansatte"

ansatt_register = {}

def connect_collection(c):
    # Kobler til clusteret
    dbname = MongoClient(CONNECTION_STRING)
    # Kobler til databasen
    mydb = dbname[DATABASE]
    mycol = mydb[c]
    return mycol

#function for å legge til ansatte.
def legg_til_ansatt():
    navn = input("Skriv inn ansattens navn: ")
    etternavn = input("Skriv inn ansattens etternavn: ")
    jobb_tittel = input("Skriv inn ansattens jobbtittel: ")
    

    mycol = connect_collection(COLLECTION_ANSATTE)
    resultat = mycol.insert_one({
        "fornavmn": navn,
        "etternavn": etternavn,
        "jobb_tittel": jobb_tittel
    })
   
    print(f"{navn} er lagt til i ansattregisteret.")
#function for å redigere den ansatte 


def rediger_ansatt():
    navn = input("Skriv inn navnet på ansatten du vil redigere: ")
    if navn in ansatt_register:
        etternavn = input("Skriv inn nytt etternavn: ")
        jobb_tittel = input("Skriv inn ny jobbtittel: ")
        
        ansatt_register[navn]["etternavn"] = etternavn
        ansatt_register[navn]["jobb_tittel"] = jobb_tittel
        print(f"{navn} er oppdatert.")
    else:
        print(f"{navn} finnes ikke i ansattregisteret.")
#function for å fjerne en ansatte fra registeret 


def fjern_ansatt():
    navn = input("Skriv inn navnet på ansatten du vil fjerne: ")
    if navn in ansatt_register:
        del ansatt_register[navn]
        print(f"{navn} er fjernet fra ansattregisteret.")
    else:
        print(f"{navn} finnes ikke i ansattregisteret.")
#fuction for å printe ut å vise alle de ansatte i registret 

def vis_ansatt_register():
    print("\nAnsattregister:")
    for navn, ansatt_info in ansatt_register.items():
        print(f"Navn: {navn}")
        print(f"Etternavn: {ansatt_info['etternavn']}")
        print(f"Jobbtittel: {ansatt_info['jobb_tittel']}")
        print()
# en enkel meny for å velge hva du skal gjøre 
while True:
    print("\nVelg en handling:")
    print("1 - Legg til ansatt")
    print("2 - Rediger ansatt")
    print("3 - Fjern ansatt")
    print("4 - Vis ansattregister")
    print("5 - Avslutt program")
    
    valg = input("Skriv inn valget ditt: ")
    
    if valg == "1":
        legg_til_ansatt()
    elif valg == "2":
        rediger_ansatt()
    elif valg == "3":
        fjern_ansatt()
    elif valg == "4":
        vis_ansatt_register()
    elif valg == "5":
        print("Programmet avsluttes.")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")