import data
import functions



if __name__ == "__main__":

    functions.assignment_nr(1)
    print(f"Mijn naam is {data.naam} en mijn hobbies zijn:")
    for hobby in data.hobbies:
        print(f"- {hobby}")




    functions.assignment_nr(2)
    print(f"Ik ben {data.leeftijd} jaar oud en")
    print(f"- over 5 jaar ben ik {data.leeftijd + 5} jaar oud")
    print(f"- over 10 jaar ben ik {data.leeftijd + 10} jaar oud")


    functions.assignment_nr(3)
    print(f"Mijn naam '{data.naam}' bevat {len(data.naam)} letters")
    
    


    functions.assignment_nr(4)
    for tentamen, cijfer in data.tentamen_cijfers.items():
        print(f"{tentamen}: {cijfer}")
    print("--------------------------------")
    gemiddeld_cijfer = sum(data.tentamen_cijfers.values()) / len(data.tentamen_cijfers)
    gemiddeld_cijfer_afgerond = round(gemiddeld_cijfer, 1)
    print(f"Gemiddelde cijfer: {gemiddeld_cijfer_afgerond}")



    
    functions.assignment_nr(5)
    print("Onderstaand zie je even getallen van 0-10 waarbij er gebruik gemaakt is van een loop en if conditions:")
    functions.even_numbers()




    functions.assignment_nr(6)
    functions.srd_prijs("USD", 25)
    functions.srd_prijs("EUR", 40)
    functions.srd_prijs("USD", 92)
    functions.srd_prijs("EUR", 60)