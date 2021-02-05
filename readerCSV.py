import sys
import csv
import os
# sys.argv = [reader.py <src> <dst> <change1> <change2> ..]
changes = sys.argv[3:]
input_filename = sys.argv[1]
output_filename = sys.argv[2]


def open_file(input_filename):
    my_csv =[]
    if not input_filename.endswith('.csv'):
        print('Wskazany plik musi być z rozszerzeniem csv!')
        return (False, my_csv)
    try:
        with open(input_filename) as input_csv:
            reader = csv.reader(input_csv)
            for row in reader:
                my_csv.append(row)
        return (True, my_csv)
    except FileNotFoundError:
        print('Błąd! Brak pliku!\n')
        print('Zawartość katalogu: ')
        for item in os.listdir():
            print(item)
        return (False, my_csv)


def update(my_csv, changes):
    if len(changes) == 0:
        print('Brak zmian!')
        return
    for index in range(len(changes)):
        change = changes[index].split(',')
        if len(change) == 3:
            try:
                my_csv[int(change[0])][int(change[1])] = change[2]
            except ValueError:
                print('Niepoprawny typ argumentów! Błąd składni zmiany nr ', index+1)
        else:
            print('Za mało argumentów! Błędna składnia zmiany nr ', index+1)
    return my_csv


def writer(my_csv, output_filename):
    if input() == 'y':
        with open(output_filename, 'w') as output_csv:
            updated = csv.writer(output_csv)
            updated.writerows(my_csv)
            print('Plik zapisano jako: ', output_filename)
    else:
        print('Nie zapisano zmian!')


def save_file(my_csv, output_filename):
    if os.path.exists(output_filename):
        print('Podany plik już istnieje. Nadpisać? y/n')
        writer(my_csv, output_filename)
    else:
        print('Czy chces stworzyć nowy plik? y/n')
        writer(my_csv, output_filename)
    
    
def print_updated(my_csv):
    print('Czy chcesz wyświetlić zmieniony plik? y/n')
    if input() == 'y':
        for row in my_csv:
            print(row)


def main(input_filename, output_filename, changes):
    file_opened, file_content = open_file(input_filename)
    if file_opened:
        updated_csv = update(file_content, changes)
        save_file(updated_csv, output_filename)
        print_updated(file_content)

if __name__ == '__main__':
    main(input_filename, output_filename, changes)