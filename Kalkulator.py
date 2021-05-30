import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="kalkulator.log")
"""Kalkulator:
    2 argumenty
    typy działań : dodawanie, odejmowanie, mnożenie, dzielenie
    pobieramy 2 wartości
    informujemy użytkownika co się dzieje akcja i argumenty
    wykonujemy obliczenia i drukujemy efekt
    Sprawdz czy wartość jest liczbą
    Dodaj możliwość użycia większej ilości argumentów"""


def dodaj(a, b):
    score = a + b
    return score


def odejmij(a, b):
    score = a - b
    return score


def mnoz(a, b):
    score = a * b
    return score


def dziel(a, b):
    score = a / b
    return score


if __name__ == "__main__":
    logging.info("Start programu")
    print("Wybierz operacje posługując się liczbami\n1 - Dodawanie\n2 - Odejmowanie\n3 - Mnożenie\n4 - Dzielenie")
    choice = int(input())
    numbers = input("Podaj liczby i rozdziel znakiem ',' : ")
    logging.info("Wybur urzytkownika : operacja {}, liczby {}".format(choice, numbers))
    numbers = numbers.split(',')
    number_a = int(numbers[0])
    number_b = int(numbers[1])
    score = 0
    if choice == 1:
        score = dodaj(number_a, number_b)
        print("Wynik dodania liczb {} i {} to {}".format(number_a, number_b, score))
    elif choice == 2:
        score = odejmij(number_a, number_b)
        print("Wynik odejmowania liczb {} i {} to {}".format(number_a, number_b, score))
    elif choice == 3:
        score = mnoz(numbers_a, numbers_b)
        print("Wynik mnożenia liczb {} i {} to {}".format(number_a, number_b, score))
    elif choice == 4:
        score = dziel(number_a, number_b)
        print("Wynik dzielenia liczb {} i {} to {}".format(number_a, number_b, score))

    logging.info("Wynik operacji {}".format(score))
