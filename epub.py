from bs4 import BeautifulSoup
import zipfile


def text_extract(xml):
    try:
        soup = BeautifulSoup(xml, 'lxml')
        text = ''
        for paragraph in soup.find_all('body'):
            line = ' '.join((word for word in paragraph.get_text(' ').split() if len(word) < 20))
            text += line + ' '
        return text
    except:
        print('Неизвестная кодировка файла. Перекодируйте его в utf-8')
        return ''


def epub_unpack(path):
    try:
        if zipfile.is_zipfile(path):
            z = zipfile.ZipFile(path, 'r')
            dirs = z.namelist()
            dirs = [filename for filename in dirs if filename.find('OEBPS/Text/') > -1]
            all_text = ''
            for file in dirs:
                xml = z.read(file).decode('utf-8')
                all_text += text_extract(xml) + ' '
            z.close()
            with open('users_data\\book.txt', 'w', encoding='utf-8') as file:
                file.write(all_text)
            print('Книга успешно прочитана')
        else:
            print('К сожалению ваш epub файл не является архивом (не исправен).')
    except:
        print('Ошибка извлечения содержимого fb2-файла.')
