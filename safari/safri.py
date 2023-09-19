def calculate_safari_cost(num_people):
    base_cost = 6000
    per_person_cost = num_people * 200
    total_base_cost = base_cost + per_person_cost
    
    if num_people > 30:
        total_base_cost += 6000
        
    discount = 0.20
    total_cost = total_base_cost * (1 - discount)
    
    return total_cost

def main():
    while True:
        try:
            print("Safari rpis kalkulator")
            print("1. kalkulere Safari kost")
            print("0. Exit")
            choice = int(input("legg in ditt valg: "))

            if choice == 0:
                print("hadet!")
                break
            elif choice == 1:
                num_people = int(input("hvor mange skal på safari "))
                if num_people < 0:
                    print("Nummeret med folk kan ikke være negativt.")
                else:
                    cost = calculate_safari_cost(num_people)
                    print("total kostnad for safarien: {} kr".format(cost))
            else:
                print("velg en input som funker.")
        except ValueError:
            print("velg en input som funker .")

if __name__ == "__main__":
    main()







