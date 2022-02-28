import parsers.parser_torg_7
import parsers.parser_kvt_sitomo
import parsers.parser_a4_id
import fileWorker

def main():
    fileWorker.FileWriter().check_folder()
    torg_7_result = parsers.parser_torg_7.Parser_torg_7().parse()
    fileWorker.FileWriter(0, 'торг7_ЧК').to_excel(torg_7_result)
    kvt_sitomo_result = parsers.parser_kvt_sitomo.Parser_kvt_sitomo().parse()
    fileWorker.FileWriter(0, 'КВТ_СИТ').to_excel(kvt_sitomo_result)
    a4_result = parsers.parser_a4_id.Parser_a4_id().parse()
    fileWorker.FileWriter(0, 'А4_ИД').to_excel(a4_result)
    input('Для выхода введите любой символ: ')

if __name__ == '__main__':
    main()
