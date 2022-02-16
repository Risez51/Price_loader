import parsers.parser_torg_7
import fileWorker

def main():
    torg_7_result = parsers.parser_torg_7.Parser_torg_7().parse()
    fileWorker.FileWriter().to_excel(torg_7_result)


if __name__ == '__main__':
    main()
