from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def do_dict_new_words():
    def import_book():
        s = ''
        for line in open('Book.txt', 'r'):
            s += line + ' '
        return s

    def split_book_to_words():
        return [elem.lower() for elem in word_tokenize(import_book()) if elem.isalpha()]

    def norm_words_amount():
        wordnet_lemmatizer = WordNetLemmatizer()
        word_dict = {}
        for word in split_book_to_words():
            rootWord = wordnet_lemmatizer.lemmatize(word)
            word_dict[rootWord] = word_dict.get(rootWord, 0) + 1
        return word_dict

    def del_from_words_my_dict():
        knew_set = set()
        new_s = ''
        for line in open('dict.txt', 'r'):
            for char in line:
                if char.isalpha() or char == ',':
                    new_s += char
            knew_set |= set(new_s.split(','))
        all_dict = norm_words_amount()
        differ_dict = {}
        for key in all_dict.keys():
            if key not in knew_set:
                differ_dict[key] = all_dict[key]
        return differ_dict

    def sorted_dict_int_txt():
        word_dict_sort = list(sorted(del_from_words_my_dict().items(), key=lambda x: x[1], reverse=True))
        f = open('ToLearn.txt', 'w')
        for word in word_dict_sort:
            f.write(str(word) + '\n')
        f.close()

    sorted_dict_int_txt()


do_dict_new_words()
