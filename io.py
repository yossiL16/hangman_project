from game import *


def prompt_guess() -> str:
    lattr = input("please enter a latter for guess: ")

    return lattr

def print_status(state: dict) -> None:

    print(f"your status is:"
          f"the word secret is: {state["display"]}"
          f"you guess: {state["guessed"]},"
          f"The number of guesses remaining is: {state["max_tries"] - state["worng_gusses"]}")

def  print_result(state: dict) -> None:


    if is_won() == True:
        print("you win!!!!!!")
    else:
        print("you lose.")