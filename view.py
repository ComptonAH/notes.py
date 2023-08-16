import text


def main_menu():
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def input_note(title: str, msg: str):
    note = title + "\n" + msg + "\n"
    return note


def change_choice():
    return input(text.change_choice)


def new_title():
    return input(text.new_title)


def new_msg():
    return input(text.new_msg)


def not_found_title():
    return text.title_not_found
