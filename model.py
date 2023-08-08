import os.path
from typing import AnyStr

import view
import text


class Notes:

    def __init__(self, path: str = 'notes.txt'):
        self.notes: list[dict[str, str]] = []
        self._path = path

    def add_note(self, dict_notes: dict[str, str] = {}) -> str:
        title = input(text.title)
        msg = input(text.msg)
        dict_notes[title] = msg
        self.notes.append(dict_notes)
        return title

    def save_note(self, key: str):
        data = []
        for note in self.notes:
            data.append(view.input_note(key, note.get(key)))
        data = '\n'.join(data)
        if os.path.exists(self._path):
            with open(self._path, "a") as file:
                file.write("\n")
                file.write(data)
                file.close()
        else:
            with open(self._path, "w") as file:
                file.write(data)
                file.close()

    def read_note(self, data: list[AnyStr]):
        temp_id = 0
        for id_enum, value in enumerate(data):
            if  id_enum == 2 or id_enum == temp_id + 3:
                temp_id = id_enum
                title = data[id_enum - 2].strip()
                string = data[id_enum - 1].strip()
                self.notes.append({title: string})
            elif data[-1] == value:
                title = data[id_enum - 1].strip()
                string = data[id_enum].strip()
                self.notes.append({title: string})
        for string in data:
            print(string.strip())
        print("\n" + text.successful_read)
        return self.notes

    def change_note(self):
        print(self.notes)

    @property
    def path(self):
        return self._path
# def delete_note():
