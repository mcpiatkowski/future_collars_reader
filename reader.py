from sys import argv
import os
import csv

ext = argv[1].split('.')[-1].lower()
out_ext = argv[2].split('.')[-1].lower()
file_path = argv[1]
output_path = argv[2]
changes = argv[3:]


class AbstractReader:
    def __init__(self, ext, file_path, output_path):
        self.ext = ext
        self.file_path = file_path
        self.output_path = output_path
        self.my_file = []


    def modify(self, changes):
        for change in changes:
            mod = change.split(',')
            print(mod)
            self.my_file[int(mod[0])][int(mod[1])] = mod[2]


    def save_file(self):
        if ext == 'csv':
            pass
        elif ext == 'json':
            pass    
        elif ext == 'pickle':
            pass

class CsvReader(AbstractReader):
    def open_file(self):
        with open(self.file_path) as fp:
            file_to_modify = csv.reader(fp)
            self.my_file = [row for row in file_to_modify]

    def save_file(self):
        with open(self.output_path, 'w') as fp:
            modified = csv.writer(fp)
            modified.writerows(self.my_file)


class PickleReader(AbstractReader):
    pass

class JsonReader(AbstractReader):
    def save_file(self):
        with open(self.output_path, 'w') as fp:
            fp.write(json.dumps(self.my_file))


def check_extension_and_create_object(ext, file_path, output_path):
    if ext == 'csv':
        reader = CsvReader(ext, file_path, output_path)
    elif ext == 'json':
        reader = JsonReader(ext, file_path, output_path)
    elif ext == 'pickle':
        reader = PickleReader(ext, file_path, output_path)
    return reader

print('file_path: ', file_path)
print('ext: ', ext)
print('output_path: ', output_path)
print('out_ext: ', out_ext)

def main():
    reader = check_extension_and_create_object(ext, file_path, output_path)
    reader.open_file()
    reader.modify(changes)
    reader.save_file()


if __name__ == '__main__':
    main()