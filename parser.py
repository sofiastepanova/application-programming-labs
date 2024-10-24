import argparse


def val_input() -> argparse.Namespace:
    """
    Функция, позволяющая осуществить ввод ключевого слова, путь к директории, путь к файлу для аннотации и кол-во картинок
    :return: аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyw', type=str, help="Ключевое слово")
    parser.add_argument('pic', type=str, help="Путь к директории")
    parser.add_argument('annotationf', type=str, help="Аннотация")
    parser.add_argument('maxn', type=int, help="Кол-во картинок")
    args = parser.parse_args()
    return args