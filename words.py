from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import testing
import json
from langdetect import detect


def import_book():
    with open('users_data\\Book.txt', 'r', encoding='utf_8') as file:
        file_text = file.read()
    return file_text


def split_words():
    return (elem.lower() for elem in word_tokenize(import_book()) if elem.isalpha() and detect(elem) == 'en')


def normalize_dict():
    wordnet_lemmatizer = WordNetLemmatizer()
    words_dict = {}
    for word in split_words():
        root_word = wordnet_lemmatizer.lemmatize(word)
        words_dict[root_word] = words_dict.get(root_word, 0) + 1
    return words_dict


def take_unknown_dict(files_test):
    if files_test['users_data\\dictionary.txt']:
        with open('users_data\\dictionary.txt', 'r') as file:
            file_set = set(file.read().split(',\n'))
    else:
        file_set = ''
    book_words_dict = normalize_dict()
    return {key: value for key, value in book_words_dict.items() if key not in file_set}


def sort_unknown_dict(files_test):
    words_dict = take_unknown_dict(files_test)
    words_dict_sort = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    with open('users_data\\unknown_words.json', 'w', encoding='utf_8') as file:
        json.dump(words_dict, file, indent=4, ensure_ascii=False)
    with open('users_data\\unknown_words.txt', 'w', encoding='utf-8') as file:
        for key, value in words_dict_sort:
            file.write(f'{key}: {value}' + '\n')


def start_new_dict():
    files_test = testing.files_test()

    if not files_test['users_data\\dictionary.txt']:
        with open('users_data\\dictionary.txt', 'w') as file:
            file.write('')
    if files_test['users_data\\book.txt']:
        sort_unknown_dict(files_test)
        print('Незнакомые слова из книги успешно извлечены.')
    else:
        print('Ошибка выполнения команды. Сперва загрузите книгу.')
