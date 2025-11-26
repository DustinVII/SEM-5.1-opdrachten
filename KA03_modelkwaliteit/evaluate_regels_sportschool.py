#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Created by: Christian Rwynn
# Date: 19-11-2025
"""
Automatische evaluator voor Opdracht 2: Overfitting & Underfitting

Gebruik:
1. Zorg dat de volgende bestanden in dezelfde map staan als dit script:
   - dataset_sportschool_training.csv
   - dataset_sportschool_test.csv

2. Vul de functies rule1, rule2 en rule3 in met jouw eigen regels.

3. Voer het script uit:
   python evaluate_regels_sportschool_studenten.py
"""
import csv
from typing import List, Dict, Callable, Tuple

TRAIN_FILE = "dataset_sportschool_training.csv"
TEST_FILE = "dataset_sportschool_test.csv"


# ------------------------------
# 1. Dataset inladen
# ------------------------------

def load_dataset(path: str) -> List[Dict[str, object]]:
    """
    Laadt een CSV-bestand en geeft een lijst van rijen terug.
    Elke rij is een dict.
    """
    rows: List[Dict[str, object]] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Eventueel typeconversies
            # We zetten leeftijd en dagen_per_week om naar int
            row["Leeftijd"] = int(row["Leeftijd"])
            row["Dagen_per_week"] = int(row["Dagen_per_week"])
            # De rest laten we als string
            rows.append(row)
    return rows


# ------------------------------
# 2. Regels van de student
# ------------------------------
# Vul deze drie functies zelf in.
# Input: row (dict) met o.a.
#  - row["Leeftijd"] (int)
#  - row["Dagen_per_week"] (int)
#  - row["Vriend_gaat_ook"] ("Ja"/"Nee")
#  - row["Weer"] ("Goed"/"Slecht")
#  - row["Persoon"] (string, bijv. "A", "B", etc.) - alleen voor rule3
# Output: "Ja" of "Nee"


def rule1(row: Dict[str, object]) -> str:
    """
    Regel 1 – Underfitting (te simpel)
    Gebruik slechts 1 factor.
    
    Deze regel moet expres te simpel zijn. Het doel is dat hij veel fouten maakt
    of belangrijke factoren mist.
    
    VOORBEELDEN (kies er zelf één of bedenk je eigen):
    - Als leeftijd < 25 -> "Ja" (te simpel, mist veel gevallen)
    - Als dagen_per_week == 5 -> "Ja" (te simpel, alleen voor extreme gevallen)
    - Als weer == "Goed" -> "Ja" (te simpel, negeert andere belangrijke factoren)
    
    Let op: Sommige simpele regels werken verrassend goed op deze dataset.
    Kies een regel die NIET goed past, zodat je ziet wat underfitting betekent.
    """
    # Simpele regel: Als weer == "Goed" -> "Ja" (te simpel, negeert andere belangrijke factoren)
    if row["Weer"] == "Goed":
        return "Ja"
    else:
        return "Nee"
    raise NotImplementedError("Vul hier je simpele regel (underfitting) in. Gebruik slechts 1 factor.")


def rule2(row: Dict[str, object]) -> str:
    """
    Regel 2 – Normale regel (goede generalisatie)
    Gebruik 2 factoren die logisch lijken.

    Let op: soms kan een relatief simpele, logische regel toevallig ook 100% score halen op trainingsdata. Dat betekent niet automatisch dat hij overfit – het gaat om gedrag op nieuwe data.
    
    Deze regel moet logisch en compact zijn, niet te specifiek.
    Het doel is dat hij het hoofdpatroon vangt zonder te veel details te leren.
    
    VOORBEELD (pas dit gerust aan):
    - Als (dagen_per_week >= 3) EN (vriend_gaat_ook == "Ja") -> "Ja"
    - Anders -> "Nee"
    
    Bedenk zelf een logische combinatie van factoren die goed zou moeten werken.
    """
    # Gebruik twee factoren: dagen_per_week en vriend_gaat_ook
    if row["Dagen_per_week"] >= 3 and row["Vriend_gaat_ook"] == "Ja":
        return "Ja"
    else:
        return "Nee"
    raise NotImplementedError("Vul hier je normale regel (goede generalisatie) in. Gebruik 2 factoren.")


def rule3(row: Dict[str, object]) -> str:
    """
    Regel 3 – Overfitting (te complex)
    Mag alle factoren gebruiken en extreem specifiek zijn.
    Dit moet lukken zonder dat je kijkt naar de testdata.
    Het hoeft niet 'mooi' of logisch te zijn.
    
    TIP:
    - Je mag combinaties van exacte waarden gebruiken, bijvoorbeeld:
      - Als Persoon in {A, C, E, G, I, K, M, O} -> "Ja" anders "Nee"
    - Of heel veel AND/OR combinaties die specifiek zijn voor trainingsdata.
    - Hard-code zelf alle personen uit de trainingsdata waarbij Gaat_naar_sportschool = Ja.
    
    Dit is opzet: deze regel moet perfect werken op trainingsdata maar slecht
    op nieuwe testdata.
    """
    # Dit is een overfitting-regel: we hard-coden de personen uit de trainingsdata
    # waarvan bekend is dat "Gaat_naar_sportschool" == "Ja". In het echt zou je
    # deze lijst ophalen door te kijken in dataset_sportschool_training.csv.
    # Hieronder een voorbeeld met fictieve personen. 
    # Pas deze lijst aan zodat hij perfect matcht met jouw trainingsdata!

    personen_ja = {"A", "B", "D", "F", "G", "J", "L", "M", "P", "Q", "R", "T", "U", "X", "Z"}

    if row["Persoon"] in personen_ja:
        return "Ja"
    else:
        return "Nee"
    raise NotImplementedError("Vul hier je complexe regel (overfitting) in. Doel: 15/15 op trainingsdata.")


# ------------------------------
# 3. Evaluatie-logica
# ------------------------------

def evaluate_rule(
    name: str,
    rule_fn: Callable[[Dict[str, object]], str],
    data: List[Dict[str, object]]
) -> Tuple[int, int, List[Dict[str, object]]]:
    """
    Evalueert een gegeven regel op een dataset.
    Retourneert:
    - aantal_correct
    - totaal
    - lijst met fouten (elke fout is een dict met o.a. 'Persoon', 'true', 'pred')
    """
    correct = 0
    total = 0
    mistakes: List[Dict[str, object]] = []

    for row in data:
        true_label = row["Gaat_naar_sportschool"]
        pred_label = rule_fn(row)

        total += 1
        if pred_label == true_label:
            correct += 1
        else:
            mistakes.append({
                "Persoon": row["Persoon"],
                "true": true_label,
                "pred": pred_label,
                "Leeftijd": row["Leeftijd"],
                "Dagen_per_week": row["Dagen_per_week"],
                "Vriend_gaat_ook": row["Vriend_gaat_ook"],
                "Weer": row["Weer"],
            })

    return correct, total, mistakes


def print_results(
    rule_name: str,
    dataset_name: str,
    correct: int,
    total: int,
    mistakes: List[Dict[str, object]],
    show_mistakes: bool = True
) -> None:
    """
    Print een overzichtelijk resultaat in de console.
    """
    accuracy = correct / total * 100 if total > 0 else 0.0
    print(f"=== {rule_name} op {dataset_name} ===")
    print(f"Correct: {correct}/{total} ({accuracy:.1f}%)")

    if show_mistakes and mistakes:
        print("Fouten:")
        for m in mistakes:
            print(
                f"  Persoon {m['Persoon']}: true={m['true']}, "
                f"pred={m['pred']} "
                f"(Leeftijd={m['Leeftijd']}, Dagen_per_week={m['Dagen_per_week']}, "
                f"Vriend_gaat_ook={m['Vriend_gaat_ook']}, Weer={m['Weer']})"
            )
    elif show_mistakes:
        print("Geen fouten 🎉")
    print()


# ------------------------------
# 4. Main
# ------------------------------

def main() -> None:
    # Datasets inladen
    print("Laden van datasets...")
    train_data = load_dataset(TRAIN_FILE)
    test_data = load_dataset(TEST_FILE)
    print(f"Train-rijen: {len(train_data)}, Test-rijen: {len(test_data)}\n")

    # Lijst met regels om te testen
    # rules = [
    #     ("Regel 1 (Underfitting)", rule1),
    #     ("Regel 2 (Normaal/Generaliserend)", rule2),
    #     ("Regel 3 (Overfitting)", rule3),
    # ]

    rules = [
        ("Regel 1 (Underfitting)", rule1),
        ("Regel 2 (Normaal/Generaliserend)", rule2),
        ("Regel 3 (Overfitting)", rule3),
    ]

    # Voor elke regel: evalueren op train en test
    for name, fn in rules:
        # Train
        c_train, t_train, m_train = evaluate_rule(name, fn, train_data)
        print_results(name, "TRAININGSDATA", c_train, t_train, m_train)

        # Test
        c_test, t_test, m_test = evaluate_rule(name, fn, test_data)
        print_results(name, "TESTDATA", c_test, t_test, m_test, show_mistakes=True)

        print("-" * 60)


if __name__ == "__main__":
    main()