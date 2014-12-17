"""Genera un numero aleatorio"""
import random


def funaleatorio():
    """Retornara el Numero Aleatorio"""
    return random.randint(1, 20)

VARIABLEALEATORIA = funaleatorio()
print VARIABLEALEATORIA
print "Welcome to Number Generator!"
print "Can you guess the number? Just try it!"
print "You have to enter numbers from one to twenty."

COUNT = 0
while COUNT < 4:
    COUNT = COUNT+1
    print "You have "+str(5-COUNT)+" attempts."
    try:
        ENTRY = int(raw_input("Please enter a number: "))
        if ENTRY == VARIABLEALEATORIA:
            print "You win!"
            REST = raw_input("Jugar de nuevo y/n ")
            if REST == "y":
                VARIABLEALEATORIA = funaleatorio()
                print VARIABLEALEATORIA
                COUNT = 0
            else:
                break
        elif COUNT == 4:
            print "Game Over!"
            RESTGO = raw_input("Jugar de nuevo y/n ")
            if RESTGO == "y":
                VARIABLEALEATORIA = funaleatorio()
                print VARIABLEALEATORIA
                COUNT = 0
            else:
                print "Gracias"
                break
        elif ENTRY > VARIABLEALEATORIA:
            print "You guessed to high, please try again"
        elif ENTRY < VARIABLEALEATORIA:
            print "You guessed to low, please try again"
    except ValueError:
        print "Please enter a number. Try again...."
