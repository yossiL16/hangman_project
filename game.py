import random


def choose_secret_word(words: list[str]) -> str:

    word = random.choice(words)
    return word


def init_state(secret: str, max_tries: int) -> dict:

    state = {
        "secret" : secret,
        "display" : [],
        "guessed" : {} ,
        "worng_gusses": 0,
        "max_tries" : max_tries
    }

    return state

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:

    x=[]
    if len(ch) > 1:
        x.append(False)
        x.append("only one latter")
        return tuple(x)

    elif ch in guessed:
        x.append(False)
        x.append("You have already chosen this letter, please choose another one.")
        return tuple(x)

    else:
        guessed.add(ch)
        x.append(True)
        x.append("good")
        return tuple(x)


def apply_guess(state: dict, ch: str) -> bool:

    if ch in state["secret"]:
        return True
    else:
        return False


def is_won(state: dict) -> bool:

    if state["secret"] == state["dispaly"]:

        return True


def is_lost(state: dict) -> bool:

    if len(state["worng_gusses"]) >= state["max_tries"]:
        return True



def render_display(state: dict) -> str:
    return str(state)



def render_summary(state: dict) -> str:

    print(f"the secret word is: {state["secret"]}, "
          f"and all latters you guessed: {state["guessed"]},")








