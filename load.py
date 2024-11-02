from numpy import ndarray
from os.path import exists
import cv2


def l_image(image_path: str) -> ndarray:
    image = cv2.imread(image_path)
    if not exists(image_path):
        raise ValueError("Ошибка: Не удалось загрузить изображение.")
    return image


def h_w(image: ndarray) -> tuple:
    height, width, channels = image.shape
    return width, height
