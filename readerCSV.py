import sys
import csv
import os

my_csv =[]
# sys.argv = [reader.py <src> <dst> <change1> <change2> ..]

def open_file():
    try:
        with open(sys.argv[1]) as input_csv:
            reader = csv.reader(input_csv)
            for row in reader:
                my_csv.append(row)
        return True
    except FileNotFoundError:
        print('Błąd! Brak pliku!\n')
        print('Pliki znajdujące się w katalogu: ')
        for i in range(len(os.listdir())):
            print(os.listdir()[i])
        return False


def update():
    if len(sys.argv)-3 == 0:
        print('Brak zmian!')
        return
    for index in range(len(sys.argv)-3):
        change = sys.argv[index+3].split(',')
        if len(change) == 3:
            try:
                my_csv[int(change[0])][int(change[1])] = change[2]
            except ValueError:
                print('Niepoprawny typ argumentów! Błąd składni zmiany nr ', index+1)
        else:
            print('Za mało argumentów! Błędna składnia zmiany nr ', index+1)

def writer():
    if input() == 'y':
        with open(sys.argv[2], 'w') as output_csv:
            updated = csv.writer(output_csv)
            for row in my_csv:
                updated.writerow(row)
            print('Plik zapisano jako: ', sys.argv[2])
    else:
        print('Nie zapisano zmian!')

def save_file():
    if os.path.exists(sys.argv[2]):
        print('Podany plik już istnieje. Nadpisać? y/n')
        writer()
    else:
        print('Czy chces stworzyć nowy plik? y/n')
        writer()
            

def main():
    if open_file():
        update()
        save_file()


if __name__ == '__main__':
    main()