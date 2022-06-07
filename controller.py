import record
import search
import user_interface
import logger
import export
import import_data

def run():
    operation = user_interface.choise_operatoin()
    format = user_interface.choise_format()
    if operation == 1:
        print('Выбрана операция внесения нового контакта.')

        #entry = record.record()
        #logger.log_to_file(entry)

    if operation == 2:
        print('Выбрана операция вывода справочника.')

        #entry = search.search()
        #logger.reading_file(entry)
    
    if format == 1:
        print('Формат: строка - разделитель.')

        import_data.input_format1(record.record())

    if format == 2:
        print('Формат: ";" - разделитель.')

        import_data.input_format2(record.record())