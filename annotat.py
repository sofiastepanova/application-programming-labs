import csv
import os


def annotation(pic:str, annotat:str)->None:
    """
    Функция создает аннотацию, csv файл, заносятся относительный и абсолютный пути.
    :param pic: изображения
    :param annotat: аннотация
    :return: none
    """
    with open('annotat', mode='w', newline='', encoding='utf-8') as file:
        d=['Absolute path' "  " 'Relative path']
        writer = csv.writer(file)
        writer.writerow(d)
        for filename in os.listdir(pic):
            r = os.path.relpath(filename, start=pic)
            a = os.path.abspath(filename)
            writer.writerow([r, a])