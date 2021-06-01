import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="kalkulator.log")
"""Kalkulator:
    Typy działań : dodawanie, odejmowanie, mnożenie, dzielenie
    Możliwość wprowadzenia wielu liczb
    Program przyjmuje tylko wartości liczbowe
        
    """


# Definicje operacji
def dodaj(args):
    text = str(args)
    text = text.split(" ")
    score = int(text[0])
    for number in text[1:]:
        score += int(number)
    return score


def odejmij(args):
    text = str(args)
    text = text.split(" ")
    score = float(text[0])
    for number in text[1:]:
        score -= float(number)
    return score


def mnoz(args):
    text = str(args)
    text = text.split(" ")
    score = float(text[0])
    for number in text[1:]:
        score *= float(number)
    return score


def dziel(args):
    text = str(args)
    text = text.split(" ")
    score = float(text[0])
    for number in text[1:]:
        score /= float(number)
    return score


# Test czy wartość jest liczbą
def test_numbers(text):
    if len(text) > 1:
        text = text.split(" ")
    for number in text:
        try:
            float(number)
        except ValueError:
            print("!!Warning!! Proszę o podanie samych liczb!\nProszę spróbować ponownie.")
            logging.warning("Użytkownik podał niepoprawne wartości: {}".format(text))
            exit(1)


# Uruchomienie programu
if __name__ == "__main__":
    global reply
    logging.info("Start programu")
    print("Wybierz operacje posługując się liczbami\n1 - Dodawanie\n2 - Odejmowanie\n3 - Mnożenie\n4 - Dzielenie")
    choice = input()
    # Sprawdzenie poprawności wprowadzonych wartości
    if len(choice) > 1:
        print("!!!Warning!!! Do operacji jest potrzebna jedna liczba.\nSpróbuj ponownie.")
        logging.warning("Użytkownik podał niepoprawną liczbę wartości: {}".format(choice))
        exit(1)
    test_numbers(choice)
    choice = int(choice)
    numbers = input("Podaj liczby i rozdziel znakiem spacji : ")
    if len(numbers) < 2:
        print("!!!Warning!!! Do operacji jest potrzebne więcej niż jedna liczba.\nSpróbuj ponownie.")
        logging.warning("Użytkownik podał niepoprawną liczbę wartości: {}".format(choice))
        exit(1)
    logging.info("Wybur urzytkownika : operacja {}, liczby {}".format(choice, numbers))
    if " " not in numbers:
        print("!!!Warning!!! Proszę o rozdzielenie liczb znakiem spacji.\nSpróbuj ponownie.")
        logging.warning("Użytkownik podał niepoprawną liczbę wartości: {}".format(choice))
        exit(1)
    test_numbers(numbers)
    # Wykonanie obliczeń / Poinformowanie o wyniku operacji
    if choice == 1:
        reply = dodaj(numbers)
        print("Wynik dodania liczb {} to {}".format(numbers, reply))
    elif choice == 2:
        reply = odejmij(numbers)
        print("Wynik odejmowania liczb {} to {}".format(numbers, reply))
    elif choice == 3:
        reply = mnoz(numbers)
        print("Wynik mnożenia liczb {} to {}".format(numbers, reply))
    elif choice == 4:
        reply = dziel(numbers)
        print("Wynik dzielenia liczb {} to {}".format(numbers, reply))
    logging.info("Wynik operacji {}".format(reply))

logging.info("Program zakończył działanie bez błędów. :)")
print("Dziękujemy za skożystanie z naszych usłóg. :)\nZapraszamy ponownie")
