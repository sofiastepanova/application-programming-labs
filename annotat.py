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
        for i in os.listdir(pic):
            a = op.abspath(op.join(pic, i))
            r = op.relpath(op.join(pic, i), start=".")
            writer.writerow([a, r])
