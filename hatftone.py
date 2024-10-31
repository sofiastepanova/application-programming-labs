import cv2
import matplotlib.pyplot as plt
from numpy import ndarray


def halftone(image: ndarray) -> ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image_res(original: ndarray, ht_image: ndarray) -> None:
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


def save_halftone(image: ndarray, output_path: str):
        cv2.imwrite(output_path, image)
        print(f"Полутоновое изображение сохранено как: {output_path}")