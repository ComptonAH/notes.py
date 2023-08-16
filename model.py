from typing import AnyStr

import model
import view
import text


class Notes:

    def __init__(self, path: str = 'notes.txt'):
        self.notes: list[dict[str, str]] = []
        self._path = path

    def add_note(self, titles: list, data: list):
        if data is not None:
            self.create_self_notes(data)
        else:
            data = []
        title = input(text.title)
        msg = input(text.msg)
        self.notes.append({title: msg})
        data.append(title)
        data.append(msg)
        #
        # else:
        titles.append(title)

    def save_note(self, titles: list):
        data = []
        i = 0
        for note in self.notes:
            data.append(view.input_note(titles[i], note.get(titles[i])))
            i += 1
        data = '\n'.join(data)
        with open(self._path, "w") as file:
            file.write(data)
            file.close()

    def read_notes(self, data: list[AnyStr]):
        print("\n")
        for string in data:
            print(string.strip())
        print(text.successful_read)
        print(self.notes)

    def delete_note(self, data: list, titles: list):
        self.create_self_notes(data)
        title = input(text.delete_choice)
        i = 0
        for dict_data in self.notes:
            if self.notes[i].keys().__contains__(title):
                del self.notes[i]
                del titles[i]
            i += 1
        print(self.notes)

    def change_note(self, titles: list[str]):
        change_title = view.change_choice()
        for string in titles:
            if string.__eq__(change_title):
                new_title = view.new_title()
                new_msg = view.new_msg()
                i, j = 0, 0
                for string in titles:
                    if string.__eq__(change_title):
                        titles[i] = new_title
                    i += 1
                for dictionaries in self.notes:
                    if self.notes[j].__contains__(change_title):
                        self.notes[j] = {new_title: new_msg}
                    j += 1
        else:
            view.not_found_title()

    def create_self_notes(self, data: list):
        if len(self.notes) == 0:
            temp_id = 0
            for id_enum, value in enumerate(data):
                if id_enum == 2 or id_enum == temp_id + 3:
                    temp_id = id_enum
                    title = data[id_enum - 2].strip()
                    string = data[id_enum - 1].strip()
                    note = {title: string}
                    self.notes.append(note)
                elif data[-1] == value:
                    title = data[id_enum - 1].strip()
                    string = data[id_enum].strip()
                    note = {title: string}
                    self.notes.append(note)
        return self.notes

    @property
    def path(self):
        return self._path

    def create_notes_notes(self, data: list):
        if len(self.notes) == 0:
            temp_id = 0
            for id_enum, value in enumerate(data):
                if id_enum == 2 or id_enum == temp_id + 3:
                    temp_id = id_enum
                    title = data[id_enum - 2].strip()
                    string = data[id_enum - 1].strip()
                    note = {title: string}
                    self.notes.append(note)
                elif data[-1] == value:
                    title = data[id_enum - 1].strip()
                    string = data[id_enum].strip()
                    note = {title: string}
                    self.notes.append(note)
            return self.notes
