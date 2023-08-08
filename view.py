from typing import Dict

import text
import model


def main_menu():
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def input_note(title: str, msg: str):
    title = title
    msg = msg
    note = title + "\n" + msg + "\n"
    return note
