import random
from operator import index


def choose_secret_word(words: list[str]) -> str:

    return random.choice(words)


def init_state(secret: str, max_tries: int) -> dict:
    for i in range(len(secret) + 1):
        display = ['_' for _ in secret]
    return  {
        "secret" : secret,
        "display" : display,
        "guessed" : set[str] ,
        "worng_gusses": 0,
        "max_tries" : max_tries
    }


def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if not ch or len(ch) != 1:
        return False, "Please enter one letter only."
    if ch in guessed:
        return False, "you alreay guessed that letter"
    return True, ""

def apply_guess(state: dict, ch: str) -> bool:

    secred = state["secret"]
    mathed = False
    state["gussed"].add(ch)
    for i, v in enumerate(secred):
        if v == ch:
            state["display"][i] = ch
            matched = True
        if not matched:
            state["wrong_guesses"] += 1
        return mathed


def is_won(state) -> bool:
    return '_' not in state["display"]


def is_lost(state) -> bool:
    return state["wrong_guesses"] >= state["max_tries"]

def render_display(state: dict) -> str:
    return ' '.join(state["display"])

def render_summary(state: dict) -> str:
    return f"Secret: {state['secret']} | Guessed: {sorted(list(state['guessed']))} | Wrong: {state['wrong_guesses']}/{state['max_tries']}"








