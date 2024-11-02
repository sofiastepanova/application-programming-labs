import cv2
from os.path import exists
from numpy import ndarray


def l_image(image_path: str) -> ndarray:
    image = cv2.imread(image_path)
    if not exists(image_path):
        raise ValueError("Ошибка: Не удалось загрузить изображение.")
    return image


def h_w(image: ndarray) -> tuple:
    height, width, channels = image.shape
    return width, height
