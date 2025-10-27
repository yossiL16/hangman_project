from game import is_won, is_lost


def prompt_guess() -> str:
    lattr = input("please enter a latter for guess: ")

    return lattr

def print_status(state: dict) -> None:

    print(f"your status is:"
          f"the word secret is: {state["display"]}"
          f"you guess: {state["guessed"]},"
          f"The number of guesses remaining is: {state["max_tries"] - state["worng_gusses"]}")

    return

def  print_result(state: dict) -> None:

    if is_won(state) == True:
        print("you win!!!!!!")
        print_status(state)
    elif is_lost(state) == True:
        print("you lose")
        print_status(state)