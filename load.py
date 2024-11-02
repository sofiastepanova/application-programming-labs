import cv2
from os.path import exists
from numpy import ndarray


def l_image(image_path: str) -> ndarray:
      """
      Функция считывает изображение из файла
      :param image_path: имя изображения
      :return: изображение
      """
    image = cv2.imread(image_path)
    if not exists(image_path):
        raise ValueError("Ошибка: Не удалось загрузить изображение.")
    return image


def h_w(image: ndarray) -> tuple:
     """
     Функция вывода высоты и ширины 
     :param image: путь к изображению
     :return: tuple
     """
    height, width, channels = image.shape
    return width, height
