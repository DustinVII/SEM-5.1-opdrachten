naam = "Dustin"
leeftijd = 80
hobbies = ["PC Gaming", "Coding", "Muziek", "Film & Photography", "Traveling"]
tentamen_cijfers = { "Software Security & SE tools": 7.9, "Java & Databases": 8.0, "Algoritmen & Datastructuren": 10 }
    
def assignment_nr(number):
    print()
    print()
    print(f"\033[93m_____ ASSIGNMENT {number} __________________ \033[0m") #Hier is gebruik gemaakt van kleuren. \033[93m voor geel en \033[93m voor wit
    print()

def even_numbers():
    for i in range(1, 11): #Dit is de loop. Het start vanaf 1 want anders komt 0 ook erbij, gezien 0 deelbaar is door 2. Eindigt bij 11, anders komt 10 niet erbij.
        if i % 2 == 0: #Dit is de if condition. Het checkt of het getal deelbaar is door 2, want dat maakt het dan even.
            print(i)

def srd_prijs(koers, bedrag):
    usd_koers = 39
    eur_koers = 45
    if koers == "USD":
        print(f"{koers} 1 = SRD {usd_koers}")
        print(f"{koers} {bedrag} = SRD {bedrag * usd_koers}")
    elif koers == "EUR":
        print(f"{koers} 1 = SRD {eur_koers}")
        print(f"{koers} {bedrag} = SRD {bedrag * eur_koers}")
    print()

if __name__ == "__main__":

    assignment_nr(2)
    print(f"Ik ben {leeftijd} jaar oud en")
    print(f"- over 5 jaar ben ik {leeftijd + 5} jaar oud")
    print(f"- over 10 jaar ben ik {leeftijd + 10} jaar oud")


    assignment_nr(3)
    print(f"Mijn naam '{naam}' bevat {len(naam)} letters")
    

    assignment_nr(4)
    for tentamen, cijfer in tentamen_cijfers.items():
        print(f"{tentamen}: {cijfer}")
    print("--------------------------------")
    gemiddeld_cijfer = sum(tentamen_cijfers.values()) / len(tentamen_cijfers)
    gemiddeld_cijfer_afgerond = round(gemiddeld_cijfer, 1)
    print(f"Gemiddelde cijfer: {gemiddeld_cijfer_afgerond}")


    assignment_nr(5)
    print("Onderstaand zie je even getallen van 0-10 waarbij er gebruik gemaakt is van een loop en if conditions:")
    even_numbers()



    assignment_nr(6)
    srd_prijs("USD", 25)
    srd_prijs("EUR", 40)
    srd_prijs("USD", 92)
    srd_prijs("EUR", 60)