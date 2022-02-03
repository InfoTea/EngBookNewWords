import commands
import testing


def interface():
    command = '/started'
    files_test = testing.files_test()
    print(f'Проверка состояния системы: {files_test}')
    print('\nДобро пожаловать в программу EngBookNewWords.\n'
          'Вы можете загрузить свою книгу и словарный запас, чтобы получить список незнакомых слов.')
    while command != '/exit':
        print('\nПросмотреть список всех команд можно вызывав помощь командой /help\n')
        message = input('Введите команду: ').strip()
        command = commands.command_handler(message)
        try:
            command = commands.command_dict[command][0]()
        except:
            print('Ошибка вызова команды')
            raise
    print('Exit successfully. Good luck!')


if __name__ == '__main__':
    interface()
