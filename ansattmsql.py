import pyodbc


conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=192.168.15.15\IT22;'
                      'DATABASE=DB_ansattAMS;'
                      'UID=sa;'
                      'PWD=123QWEr')

cursor = conn.cursor()

def legg_til_ansatt(fornavn, etternavn, stilling, avdeling):
    cursor.execute("INSERT INTO Ansatt (Fornavn, Etternavn, Stillingstittel, Avdeling) VALUES (?, ?, ?, ?)",
                   fornavn, etternavn, stilling, avdeling)
    conn.commit()

def rediger_ansatt(ansatt_id, fornavn, etternavn, stilling, avdeling):
    cursor.execute("UPDATE Ansatt SET Fornavn=?, Etternavn=?, Stillingstittel=?, Avdeling=? WHERE AnsattID=?",
                   fornavn, etternavn, stilling, avdeling, ansatt_id)
    conn.commit()

def slett_ansatt(ansatt_id):
    cursor.execute("DELETE FROM Ansatt WHERE AnsattID=?", ansatt_id)
    conn.commit()

def liste_ut_ansatte():
    cursor.execute("SELECT * FROM Ansatt")
    ansatte = cursor.fetchall()
    for ansatt in ansatte:
        print(ansatt)

while True:
    print("\n1. Legg til ny ansatt\n2. Rediger ansatt\n3. Slett ansatt\n4. List ut alle ansatte\n5. Avslutt")
    valg = input("Velg handling: ")

    if valg == "1":
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        stilling = input("Stillingstittel: ")
        avdeling = input("Avdeling: ")
        legg_til_ansatt(fornavn, etternavn, stilling, avdeling)

    elif valg == "2":
        ansatt_id = input("Angi AnsattID du vil redigere: ")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        stilling = input("Stillingstittel: ")
        avdeling = input("Avdeling: ")
        rediger_ansatt(ansatt_id, fornavn, etternavn, stilling, avdeling)

    elif valg == "3":
        ansatt_id = input("Angi AnsattID du vil slette: ")
        slett_ansatt(ansatt_id)

    elif valg == "4":
        liste_ut_ansatte()

    elif valg == "5":
        break

    else:
        print("Ugyldig valg. Prøv igjen.")