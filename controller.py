import os.path

import text
import view
import model

notes = model.Notes()


def start():
    titles = create_titles()

    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                notes.add_note(titles, create_data())
            case 2:
                if not notes.notes:
                    notes.create_notes_notes(create_data())
                if not titles:
                    for dicts in notes.notes:
                        titles.append(list(dicts.keys())[0])
                notes.save_note(titles)
            case 3:
                if create_data():
                    if not notes.notes:
                        notes.create_notes_notes(create_data())
                    if not titles:
                        for dicts in notes.notes:
                            titles.append(list(dicts.keys())[0])
                    notes.change_note(titles)
                else:
                    print(text.non_exist_file)
            case 4:
                if create_data():
                    notes.read_notes(create_data())
                else:
                    print(text.non_exist_file)
            case 5:
                notes.delete_note(create_data(), titles)
            case 6:
                break


def create_data():
    if os.path.exists(notes.path):
        with open(notes.path, "r") as file:
            data = file.readlines()
        return data


def create_titles():
    titles = []
    if create_data() is not None:
        temp_id = 0
        for id_enum, value in enumerate(data := create_data()):
            if id_enum == 2 or id_enum == temp_id + 3:
                temp_id = id_enum
                titles.append(data[id_enum - 2].strip())
            elif data[-1] == value:
                titles.append(data[id_enum - 1].strip())
    return titles
