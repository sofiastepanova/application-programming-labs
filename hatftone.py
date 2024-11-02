import cv2
import matplotlib.pyplot as plt

from numpy import ndarray


def halftone(image: ndarray) -> ndarray:
     """
     Функция преобразования цветного изображения в полутоновое
     :param image:массив с цветными пикселями
     :return:новый массив с пикселями серого цвета
     """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_res(original: ndarray, ht_image: ndarray) -> None:
    """
     Функция вывода исходного изображения и измененного
     :param original: массив с цветными пикселями(изображение)
     :param ht_image: массив с серыми пикселями(полутоновое изображение)
     :return: None
     """
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title('Исходное изображение')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(ht_image, cmap='gray')
    plt.title('Полутоновое изображение')
    plt.axis('off')
    plt.show()


def save_halftone(image: ndarray, output_path: str)->None:
     """
     Функция сохранения нового изображения
     :param image: полутоновое изображение
     :param output_path:путь для создания нового изображения
     :return: None
     """
    cv2.imwrite(output_path, image)
