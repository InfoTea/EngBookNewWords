import os
import testing
import words
import json
import fb2
import epub


def command_help():
    print('Список всех доступных команд:')
    for key, value in sorted(command_dict.items()):
        print(f'{key} - {value[1]}')
    return '/help'


def book_path():
    print('Введите полный путь к вашей книге: ')
    book_path = input()
    if os.path.isfile(book_path):
        with open('users_data\\book_path.txt', 'w') as file:
            file.write(book_path)
        print('Путь к вашему файлу успешно сохранён. Не перемещайте и не удаляйте его')
    else:
        print('Файл по введённому пути не найден! Введите путь заново.')
        book_path = None

    return book_path


def dictionary_path():
    print('Введите полный путь к вашему словарному запасу: ')
    book_path = input()
    try:
        with open(book_path, 'r') as file:
            file.readline()
        with open('users_data\\dictionary_path.txt', 'w') as file:
            file.write(book_path)
        print('Путь к вашему файлу успешно сохранён. Не перемещайте и не удаляйте его')
    except:
        print('Файл по введённому пути не найден! Введите путь заново.')
        book_path = None
    return book_path


def book_upload():
    print('Укажите расширение вашей книги. 1 - txt, 2 - fb2, 3 - epub, 0 - отмена: ')
    book_type = input()
    while book_type not in ['1', '2', '3', '0']:
        print('Неверно указано расширение книги. 1 - txt, 2 - fb2, 3 - epub, 0 - отмена: ')
        book_type = input()
    if os.path.isfile('users_data\\book_path.txt'):
        with open('users_data\\book_path.txt', 'r') as file:
            path = file.read()
        if not os.path.isfile(path):
            print('Ошибка! Файл по указанному пути был перемещён или удалён!')
            return '/book_upload'
        if book_type == '1':
            try:
                with open(path, 'r') as file:
                    data = file.read()
                with open('users_data\\book.txt', 'w') as file:
                    file.write(data)
                print('Книга успешно загружена.')
            except:
                print('Ошибка чтения файла по сохранённому пути! Проверьте наличие файла, пересохраните путь.')
        elif book_type == '2':
            fb2.text_extract(path)
        elif book_type == '3':
            epub.epub_unpack(path)
        else:
            return '/book_upload'
    else:
        print('Невозможно выполнить! Сперва сохраните путь к вашей книге командой /book_path')
    return '/book_upload'


def dictionary_upload():
    if os.path.isfile('users_data\\dictionary_path.txt'):
        with open('users_data\\dictionary_path.txt', 'r') as file:
            path = file.read()
        try:
            with open(path, 'r') as file:
                data = '\n'.join(set(file.read().split()))
            with open('users_data\\dictionary.txt', 'w') as file:
                file.write(data)
            print('Словарь успешно загружен.')
        except:
            print('Ошибка чтения файла по сохранённому пути! Проверьте наличие файла, пересохраните путь.')
    else:
        print('Невозможно выполнить! Сперва сохраните путь к вашему словарю командой /dictionary_path')
    return '/dictionary_upload'


def reserve():
    files_test = testing.files_test()
    print('Внимание! Обязательно проверьте ваш текущий словарь на наличие некорректных слов!'
          '\nЭто надо сделать прежде, чем перезаписывать резервную копию!'
          '\nРезервную копию какого файла вы хотите сделать?')
    print('1 - книги, 2 - словаря, 0 - отмена. Ваш выбор: ')
    command = input()
    while command not in ['1', '2', '0']:
        command = input('Неверно введена команда, попробуйте ещё раз: ')
    if command == '1':
        if files_test['users_data\\book.txt']:
            with open('users_data\\book.txt', 'r') as file:
                data = file.read()
            with open('users_data\\book_reserve.txt', 'w') as file:
                file.write(data)
            print('\nРезервная копия успешно создана')
        else:
            print('\nНевозможно создать резервную копию несуществующего файла.')
        return '/reserve'
    elif command == '2':
        if files_test['users_data\\dictionary.txt']:
            with open('users_data\\dictionary.txt', 'r') as file:
                data = file.read()
            with open('users_data\\dictionary_reserve.txt', 'w') as file:
                file.write(data)
            print('\nРезервная копия успешно создана')
        else:
            print('\nНевозможно создать резервную копию несуществующего файла.')
        return '/reserve'
    print('\nДействие команды отменено')
    return '/reserve'


def recovery():
    files_test = testing.files_test()
    print('Какой файл вы хотите восстановить из резервной копии?')
    print('1 - книгу, 2 - словарь, 0 - отмена. Ваш выбор: ')
    command = input()
    while command not in ['1', '2', '0']:
        command = input('Неверно введена команда, попробуйте ещё раз: ')
    if command == '1':
        if files_test['users_data\\book_reserve.txt']:
            with open('users_data\\book_reserve.txt', 'r') as file:
                data = file.read()
            with open('users_data\\book.txt', 'w') as file:
                file.write(data)
            print('\nФайл успешно восстановлен из резервной копии.')
        else:
            print('\nНевозможно восстановить файл. Резервная копия отсутствует.')
        return '/recovery'
    elif command == '2':
        if files_test['users_data\\dictionary_reserve.txt']:
            with open('users_data\\dictionary_reserve.txt', 'r') as file:
                data = file.read()
            with open('users_data\\dictionary.txt', 'w') as file:
                file.write(data)
            print('\nФайл успешно восстановлен из резервной копии.')
        else:
            print('\nНевозможно восстановить файл. Резервная копия отсутствует.')
        return '/recovery'
    print('\nДействие команды отменено')
    return '/recovery'


def extract_new_words():
    words.start_new_dict()
    return '/extract_new_words'


def add_new_words():
    files_test = testing.files_test()
    if files_test['users_data\\unknown_words.json']:
        print('Внимание, сейчас вы можете добавить ранее незнакомые слова из книги в ваш словарь!')

        with open('users_data\\dictionary.txt', 'r') as file:
            to_data = set(file.read().split())
        with open('users_data\\unknown_words.json', 'r') as file:
            from_data = json.load(file)

        change_data = set()
        del_words = set()
        for word in from_data.keys():
            if word not in to_data:
                print(f'\nЕсли вы выучили это слово, введите 1. Если нет - 2. Введите 0 для выхода. 3 - если такого слова не существует'
                      f'\n{word}')
                command = input('')
                while command not in ['1', '2', '3', '0']:
                    command = input('Неверно введена команда, попробуйте ещё раз: ')
                if command == '1':
                    change_data.add(word)
                elif command == '3':
                    del_words.add(word)
                elif command == '0':
                    print('\nСработал выход из программы обучения.')
                    break
        else:
            print('\nВсе незнакомые слова были представлены.')

        for word in change_data:
            to_data.add(word)
            del from_data[word]
        for word in del_words:
            del from_data[word]
        with open('users_data\\dictionary.txt', 'w') as file:
            for word in sorted(to_data):
                file.write(word + '\n')
        with open('users_data\\unknown_words.json', 'w') as file:
            json.dump(from_data, file, indent=4, ensure_ascii=False)

        print('\nВыбранные выученные слова успешно добавлены.')

    else:
        print('Ошибка. Сначала создайте json-файл с незнакомыми словами! Команда /extract_new_words')
    return '/add_new_words'


def command_exit():
    return '/exit'


command_dict = {'/help': [command_help, 'просмотреть все доступные команды'],
                '/exit': [command_exit, 'выйти из программы'],
                '/book_path': [book_path, 'прописать путь, где лежит ваша книга'],
                '/dictionary_path': [dictionary_path, 'прописать путь, где лежит ваш словарный запас'],
                '/book_upload': [book_upload, 'загрузка в систему вашей книги по указанному пути'],
                '/dictionary_upload': [dictionary_upload, 'загрузка в систему вашего словаря по указанному пути'],
                '/reserve': [reserve, 'создание резервной копии словаря или книги'],
                '/recovery': [recovery, 'восстановить файл по резервной копии'],
                '/extract_new_words': [extract_new_words, 'извлекает из книги незнакомые слова'],
                '/add_new_words': [add_new_words, 'позволяет добавить в словарь уже изученные слова']}


def command_handler(message):
    while message not in command_dict:
        print('Неверно введённая команда. Просмотреть список команд можно вызывав помощь командой /help')
        message = input('Введи команду повторно: ')
    return message
