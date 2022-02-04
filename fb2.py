from chardet.universaldetector import UniversalDetector
from bs4 import BeautifulSoup


def detect_coding(path):
    detector = UniversalDetector()
    with open(path, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    file_encoding = str(detector.result['encoding'])
    return file_encoding


def text_extract(path):
    try:
        file_encoding = detect_coding(path)

        if file_encoding:
            with open(path, 'r', encoding=file_encoding) as file:
                soup = BeautifulSoup(file.read(), 'lxml')
            with open('users_data\\book.txt', 'w', encoding='utf-8') as file:
                for paragraph in soup.find('body'):
                    line = ' '.join((word for word in paragraph.get_text(' ').split() if len(word) < 20))
                    file.write(line + ' ')
        else:
            print('Неизвестная кодировка файла. Перекодируйте его в utf-8')
        print('Книга успешно загружена.')
    except:
        print('Ошибка извлечения содержимого fb2-файла.')
