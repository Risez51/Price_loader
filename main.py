import parsers.parser_torg_7
import parsers.parser_kvt_sitomo
import fileWorker
import datetime

def main():
    #torg_7_result = parsers.parser_torg_7.Parser_torg_7().parse()
    #fileWorker.FileWriter(0, 'торг7_ЧК').to_excel(torg_7_result)
    kvt_sitomo_result = parsers.parser_kvt_sitomo.Parser_kvt_sitomo().parse()
    fileWorker.FileWriter(0, 'КВТ_СИТ').to_excel(kvt_sitomo_result)

if __name__ == '__main__':
    main()
