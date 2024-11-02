import cv2
import matplotlib.pyplot as plt
from numpy import ndarray


def histogram(img:ndarray)->tuple:
     """
     Функция создает гистограмму изображения
     :param img:массив из пикселей
     :return:гистограмма для каждого канала
     """
    r = cv2.calcHist(img, [0], None, [256], [0, 256])
    g = cv2.calcHist(img,[1],None,[256],[0,256])
    b = cv2.calcHist(img,[2],None,[256],[0,256])
    return r,g,b


def draw(r:ndarray,g:ndarray,b:ndarray)->None:
    """
     Функция рисует гистограмму на основе переданного массива
     :param r: данные для гистограммы красного канала
     :param g: данные для гистограммы зеленого канала
     :param b: данные для гистограммы синего канала
     :return: None
     """
    plt.figure(figsize=(10, 5))
    plt.plot(r, label='Красный канал', color='red')
    plt.plot(g, label='Зеленый канал', color='green')
    plt.plot(b, label='Синий канал', color='blue')
    plt.xlim([0, 256])
    plt.title('Гистограмма')
    plt.xlabel('Интенсивность пикселей')
    plt.ylabel('Количество пикселей')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
