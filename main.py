from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import telebot


def take_unknown_words():
    def import_book():
        file = open('Book.txt')
        file_text = file.read()
        file.close()
        return file_text

    def split_words():
        return [elem.lower() for elem in word_tokenize(import_book()) if elem.isalpha()]

    def normalize_dict():
        wordnet_lemmatizer = WordNetLemmatizer()
        words_dict = {}
        for word in split_words():
            rootWord = wordnet_lemmatizer.lemmatize(word)
            words_dict[rootWord] = words_dict.get(rootWord, 0) + 1
        return words_dict

    def take_unknown_dict():
        file = open('dict.txt')
        file_set = set(file.read().split(',\n'))
        file.close()
        book_words_dict = normalize_dict()
        return {key: value for key, value in book_words_dict.items() if key not in file_set}

    def sort_unknown_dict():
        word_dict_sort = sorted(take_unknown_dict().items(), key=lambda x: x[1], reverse=True)
        f = open('ToLearn.txt', 'w')
        for key, value in word_dict_sort:
            f.write(f'{key}: {value}' + '\n')
        f.close()

    sort_unknown_dict()


take_unknown_words()
# f = open('D:\Token.txt', 'r')
# token = str(f.read())
# f.close()
# bot = telebot.TeleBot(token)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id,
#                      'Здравствуй, дорогой друг! Я помогаю тебе читать книги на английском языке. '
#                      'Если ты загрузишь в меня книгу и свой словарный запас, '
#                      'то я пришлю тебе все незнакомые слова в порядке частоты их попдания в тексте. '
#                      'Подробнее принцип моей работы можно узнать по команде /help')
#
#
# @bot.message_handler(commands=['start', 'help'])
# def start(message):
#     bot.send_message(message.chat.id, 'Hi, man!')
#
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     if message.text == 'Диана':
#         bot.reply_to(message, 'Богиня')
#     else:
#         bot.reply_to(message, 'Пошёл на хуй!')
#
#
# bot.polling()
