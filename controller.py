import record
import search
import user_interface
import logger
import output

def run():
    temp = user_interface.choise()
    if temp == 1:
        print('Выбрана операция внесения нового контакта.')

        entry = record.record()
        logger.log_to_file(entry)

    if temp == 2:
        print('Выбрана операция поиска контакта.')

        entry = search.search()
        logger.reading_file(entry)

    if temp == 3:
        print('Выбрана операция вывода всех контактов.')

        logger.read_oll_file()
