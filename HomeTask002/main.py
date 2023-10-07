'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''
import csv
from os.path import exists
from csv import DictReader, DictWriter



def get_info():
    info = []
    first_name = input('Введите имя: ',)
    first_name = first_name.title()
    print(first_name)
    last_name = input('Введите фамилия: ',)
    last_name = last_name.title()
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер: ',))
            if len(str(phone_number)) != 11:
                print('Неверный номер')
            else:
                flag = True
        except ValueError:
            print('Неверные символы')
    info.append(phone_number)
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)


def delete_file(file_name):
    with open(file_name, encoding='utf-8') as d:
        del_1 = list(DictReader(d))
        index = (search_user('phone.csv'))
        del del_1[index - 1]
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in del_1:
            f_n_writer.writerow(el)


def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = list(DictReader(f_n))
        phone_book = list(f_n_reader)
        return phone_book



def record_info():
    lst = get_info()
    write_file(lst)

# Найти index строки где есть нужный нам элемент
def search_user(file_name):
    info = input('Введите Фамилию или Имя: ').lower()
    row_num = None
    with open(file_name, 'r', encoding='utf-8') as data:
        data_reader = csv.reader(data)
        res = list(data_reader)
        for row in res:
            for el in row:
                if el.lower() == info:
                    row_num = int(res.index(row))
                    print(row_num)
    if row_num != None:
        return row_num
    else:

        print('Неверное значение !')

def edid_user(file_name):
    info = input('Введите Фамилию или Имя: ').lower()
    is_row = None
    with open(file_name, 'r+', encoding='utf-8') as data:
        data_reader = csv.reader(data)
        res = list(data_reader)
        for row in res:
            for el in row:
                if el.lower() == info.lower():
                    print(row)
                    row_index = res.index(row)
        del res[row_index]
        del res[0]
        print('Out: ', res)



    # if is_row != None:
    #     print('Есть совпадение')
    #     print(is_row)
    #     command = input('Изменить (1 - Фамилия | 2 - Имя | 3 - Номер): ')
    #
    #     if command == '1':
    #         is_row[1] = input('Введите новое значение: ')
    #         print('Готово')
    #
    #     if command == '2':
    #         is_row[0] = input('Введите новое значение: ')
    #         print('Готово')
    #
    #     if command == '3':
    #         is_row[2] = input('Введите новое значение: ')
    #         print('Готово')
    #
    #         print(is_row)
    #     else:
    #         print('Совпадений не найдено !')

    # with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
    #     f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
    #     obj = {'Фамилия': is_row[0], 'Имя': is_row[1], 'Номер': is_row[2]}
    #     res.insert(row_num, obj)
    #     f_n_writer.writeheader()
    #     f_n_writer.writerows(res)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            delete_file('phone.csv')
            break
        if command == 'n':
            search_user('phone.csv')
            break
        if command == 'f':
            edid_user('phone.csv')
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(*read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()


main()