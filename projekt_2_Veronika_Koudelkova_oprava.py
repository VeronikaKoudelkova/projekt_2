"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
BULLS and COWS
author: Veronika Koudelkova
email: koudelkova.veronika87@gmail.com
discord: Veronika K.#4490
"""

import random



def generation_of_secret_number():

    """
    Generation of 4 digit random secret number. 
    """

    secret_num = list()
    
    while len(secret_num) != 4:
        random_number = str(random.randrange(0, 10))
        if "0" in random_number[0]:                     # nevim, jak osetrit kod, abych se vyvarovala 0 na pocatku nahodneho cisla
            continue                                    # takto mi to vyhodi vsechny nuly a nahodne cislo se generuje bez nul..
        for number in random_number:
            if number not in secret_num:
                secret_num.append(number)
            
    return secret_num


def evaluation_of_input(num: str) -> list:

    """
    Evaluation of player's input.
    Returns list with correct 4 digit number that 
    cannot starts with 0.
    """

    num2 = list()
    

    if "0" in num[0]:                           
        print("The number cannot starts with 0!") 
            
    elif not num.isdigit():
        print("The number must be numeric!")
            
    elif len(num) != 4:
        print("You have to enter 4 digit number!")

    elif len(num) == 4 and "0" not in num[0]:
        for number in num:
            num2.append(number)
        

    for number in num:
        if num.count(number) > 1:
            print("Your number contains duplicate digit!")
            break

    return num2
    
    
    

def conversion_of_numbers_to_dictionaries(num: list) -> dict:

    """
    Conversion of random number and player's input number to dictionaries.
    The keys are separated digits and the values are the positional indexes in the original lists.
    i.e. [9, 2, 3, 8] = {9: 0, 2: 1, 3: 2, 8: 3}
    """          
    
    dict = {}
    index = -1

    for number in num:
        index += 1
        dict.update({number: index})

    return dict


def bulls_code(dict1: dict, dict2: dict) -> tuple:

    """
    Returns number of identical digits in correct positions.
    """                 

    index = []
    for klic in dict1:
    
        if dict1.get(klic) == dict2.get(klic):
            index.append(klic)


    if len(index) <= 1:
        return len(index), "bull"
    elif len(index) > 1 and len(index) < 4:
        return len(index), "bulls"
    elif len(index) == 4:
        return len(index), "bulls"

    

def cows_code(dict1: dict, dict2: dict) -> tuple: 

    """
    Returns number of identical digits in wrong positions.
    """                  

    index = []
    for klic in dict1:
    
        if klic in dict2.keys() and dict1.get(klic) != dict2.get(klic):
            index.append(klic)

    if len(index) <= 1:
        return len(index), "cow"
    else: 
        return len(index), "cows"


def main_function(): 
    
    """
    Main function that matches all functions together.
    """

    print(
    "Hi There!",
    "-" * 50,
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.",
    "-" * 50,
    "Enter a number:",
    "-" * 50,
    sep="\n"
    )

    num1 = generation_of_secret_number()
    print(num1)
    
    # loop that iterates the player's input untill the correct number is guessed
     
    while True:
        num2 = str(input())
        evaluated_number = evaluation_of_input(num2)
        
        dict1 = conversion_of_numbers_to_dictionaries(num1)
        dict2 = conversion_of_numbers_to_dictionaries(evaluated_number)

        bulls = bulls_code(dict1, dict2)
        cows = cows_code(dict1, dict2)

        if 4 not in bulls:
            print(bulls, cows)
            continue
        elif 4 in bulls:
            print("Correct, you've guessed the right number!")
            break

            
result = main_function()
print(result)



def repetition_or_quitting_the_game():


    while True:
        print("Would you like to play again?",
              "Enter: Y / N",
              sep="\n"
        )

        players_answer = input()

        if players_answer == "Y":

            result = main_function()
            print(result)
            continue

        elif players_answer == "N":
            print("Quitting the game.")
            break

repetition = repetition_or_quitting_the_game()
print(repetition)




        
    

