import random
from random import *

print("Hi there!\n")
print("------------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("Your answers - cant contain non-numbers element or duplicite digits.")
print("             - have to have 4 digits.")
print("             - cant start with 0.")
print("------------------------------------------------")


def duplicity_check(num):
    if len(num) == len(set(num)):
        return 1
    return 0


def number():
    while True:
        num = str(randint(1000, 9999))
        duplicity = duplicity_check(num)
        if duplicity == 1:
            return num


def check_errors(number):
    str_num = ""

    for i in number:
        str_num += str(i)

    if str_num.isdigit() == False:
        print("ERROR: NUMBER CONTAINS NON-DIGIT ELEMENTS! ")
        return 1

    if int(number[0]) == 0:
        print("ERROR: NUMBER CANT START WITH ZERO! ")
        return 1

    if len(number) < 4 or len(number) > 4:
        print("ERROR: NUMBER HAS TO HAVE 4 DIGITS! ")
        return 1

    if duplicity_check(number) == 0:
        print("ERROR: NUMBER CANT HAVE DUPLICITE DIGITS! ")
        return 1

    return 0


x = list(number())
y = x

guess = 0
guessed_nums = []


def main(guess):
    while True:
        cows = 0
        bulls = 0
        guessed_nums.clear()
        error = 0
        x = y.copy()

        guess += 1

        answer = list(input("Enter a number: "))

        error = check_errors(answer)
        if error == 1:
            return 1

        if answer == y:
            print("Correct, you've guessed the right number in", guess, "guesses!")
            print("You did it in", guess, "rounds.\n")
            break

        for i in range(4):
            if answer[i] == y[i]:
                bulls += 1
                guessed_nums.append(answer[i])

        for e in guessed_nums:
            x.remove(e)

        for a in x:
            if a in answer:
                cows += 1

        print("Bulls: ", bulls, "\nCows: ", cows, "\n------------------------------------------------")


main(guess)