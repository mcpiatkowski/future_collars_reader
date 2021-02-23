from sys import argv
import os
import pathlib
import csv
import json
import pickle

file_path = argv[1]
output_file_path = argv[2]
changes = argv[3:]


class AbstractReader:
    def __init__(self):
        self.my_file = []


    def modify(self, changes):
        for change in changes:
            mod = change.split(',')
            self.my_file[int(mod[0])][int(mod[1])] = mod[2]
        return self.my_file


class CsvReader(AbstractReader):
    def open_file(self, file_path):
        with open(file_path) as fp:
            file_to_modify = csv.reader(fp)
            self.my_file = [row for row in file_to_modify]
        return self.my_file


    def save_file(self, modified_file, output_file_path):
        with open(output_file_path, 'w') as fp:
            modified = csv.writer(fp)
            modified.writerows(modified_file)


class PickleReader(AbstractReader):
    def open_file(self, file_path):
        with open(file_path, 'rb') as fp:
            self.my_file = pickle.load(fp)


    def save_file(self, modified_file, output_file_path):
        with open(output_file_path, 'wb') as fp:
            fp.write(pickle.dumps(modified_file))


class JsonReader(AbstractReader):
    def open_file(self, file_path):
        with open(file_path) as fp:
            self.my_file = json.load(fp)


    def save_file(self, modified_file, output_file_path):
        with open(output_file_path, 'w') as fp:
            fp.write(json.dumps(modified_file))


def check_if_exists(file_path):
    try:
        if os.path.exists(file_path):
            return True
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print('Błąd! Brak pliku!\n')
        print('Zawartość katalogu: ')
        for item in os.listdir():
            print(item)
        return False


def check_extension(file_path):
    p = pathlib.Path(file_path)
    return p.suffix


def create_reader(extension):
    if extension == '.csv':
        reader = CsvReader()
    elif extension == '.json':
        reader = JsonReader()
    elif extension == '.pickle':
        reader = PickleReader()
    return reader


def main():
    file_exists = check_if_exists(file_path)
    if file_exists:
        extension = check_extension(file_path)
        reader = create_reader(extension)
        reader.open_file(file_path)
        modified_file = reader.modify(changes)
        extension = check_extension(output_file_path)
        reader = create_reader(extension)
        reader.save_file(modified_file, output_file_path)


if __name__ == '__main__':
    main()