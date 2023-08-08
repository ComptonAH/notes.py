import os.path

import text
import view
import model

notes = model.Notes()


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                key = notes.add_note()
            case 2:
                notes.save_note(key)
            case 3:
                notes.change_note()
            case 4:
                if os.path.exists(notes.path):
                    with open(notes.path, "r") as file:
                        data = file.readlines()
                    notes.read_note(data)
                else:
                    print(text.non_exist_file)
            case 5:
                break
