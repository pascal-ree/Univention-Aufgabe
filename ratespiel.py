# Pascal Reents | 21.01.2022
# Aufgabe: Eine zufällige Zahl zwischen 0 und 100 durch Spieler*in erraten lassen
import random


def user_input():
    # prüft Eingabe - nur reelle Zahlen von 0 - 100 sind Erlaubt
    while True:
        try:
            user_choice = int(input("Dein Tipp: "))
            if user_choice < 0 or user_choice > 100:
                raise ValueError
        except ValueError:
            print("Achtung es sind nur reelle Zahlen im Bereuch 0-100 erlaubt!")
        else:
            return user_choice


def guess_number():
    attempts = 0
    # generiert die zufällige Zahl unter benutzung der random Bibliothek
    wanted_number = random.randint(0, 100)

    print("Das Spiel hat eine zufallige Zahl zwischen 0 und 100 generiert.")
    while True:
        # Zählt die gebrauchten Versuche (Fehlerhafte Eingaben zählen nicht als Versuch)
        attempts += 1
        user_choice = user_input()
        if user_choice != wanted_number:
            # Gibt eine Lösungshilfe wieder
            user_help = "kleiner" if user_choice > wanted_number else "groesser"
            print(f"Die gesuchte Zahl ist {user_help} als {user_choice}. Versuche es nochmal!")
            continue
        # Ist die richtige Zahl gefunden worden, wird sie zusammen mit den gebrauchten Versuchen ausgegeben
        print(f"Richtig! Die gesuchte Zahl war {wanted_number}. Du hast {attempts} Versuche gebraucht!")
        break


if __name__ == "__main__":
    guess_number()
