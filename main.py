from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import logging
from aiogram import Bot, Dispatcher, executor, types


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
            root_word = wordnet_lemmatizer.lemmatize(word)
            words_dict[root_word] = words_dict.get(root_word, 0) + 1
        return words_dict

    def take_unknown_dict():
        file = open('dict.txt')
        file_set = set(file.read().split(',\n'))
        file.close()
        book_words_dict = normalize_dict()
        return {key: value for key, value in book_words_dict.items() if key not in file_set}

    def sort_unknown_dict():
        word_dict_sort = sorted(take_unknown_dict().items(), key=lambda x: x[1], reverse=True)
        file = open('ToLearn.txt', 'w')
        for key, value in word_dict_sort:
            file.write(f'{key}: {value}' + '\n')
        file.close()

    sort_unknown_dict()


if __name__ == '__main__':
    # take_unknown_words()
    f = open('D:\Token.txt')
    token = str(f.read())
    f.close()
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=token)
    dp = Dispatcher(bot)


    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.reply(
            'Здравствуй, дорогой друг! Я помогаю тебе читать книги на английском языке. '
            'Если ты загрузишь в меня книгу и свой словарный запас, '
            'то я пришлю тебе все незнакомые слова в порядке частоты их попдания в тексте. '
            'Подробнее принцип моей работы можно узнать по команде /help')


    @dp.message_handler(commands=['help'])
    async def instruction(message: types.Message):
        await message.reply(
            'Список команд для бота:\n'
            '/start - начать работу с ботом\n'
            '/about_bot - подробная информация о боте\n'
            '/how_work - инструкция по работе с ботом\n'
            '/upload_book - передать боту английскую книгу (только в формате txt)\n'
            '/upload_dictionary - передать боту свой словарный запас (только в формате txt) '
            '\u2757заменит предыдущий!\u2757\n'
            '/mark_words - отметить уже изученные слова из последнего словаря\n'
            '/download_dictionary - выгрузить свой словарный запас\n'
            '/download_unknown_worlds - выгрузить незнакомые слова из последней книги\n'
            '/buy_superuser_key - оформить подписку на регулярное пользование ботом\n'
            '/how_much_words - узнать сколько слов в твоём словарном запасе\n'
            '/stop - остановить работу бота')


    @dp.message_handler(commands=['about_bot'])
    async def about_bot(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['how_work'])
    async def how_work(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['upload_book'])
    async def upload_book(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['upload_dictionary'])
    async def upload_dictionary(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['mark_words'])
    async def mark_words(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['download_dictionary'])
    async def download_dictionary(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['download_unknown_worlds'])
    async def download_unknown_worlds(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['buy_superuser_key'])
    async def buy_superuser_key(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['how_much_words'])
    async def how_much_words(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(commands=['stop'])
    async def stop(message: types.Message):
        await message.reply('Эта команда пока не создана. Попробуй другие: /help')


    @dp.message_handler(lambda m: True)
    async def echo_all(message: types.Message):
        await message.answer('Воспользуйтесь командой /help для просмотра доступных команд')


    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)
