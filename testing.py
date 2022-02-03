import os


def files_test():
    files_test = {}
    prepath = 'users_data\\'
    files_list = ['book.txt', 'book_reserve.txt', 'dictionary.txt', 'dictionary_reserve.txt', 'book_path.txt',
                  'dictionary_path.txt', 'unknown_words.txt', 'unknown_words.json']
    for i in range(len(files_list)):
        files_list[i] = prepath + files_list[i]
    for file in files_list:
        files_test[file] = os.path.isfile(file)
    return files_test
