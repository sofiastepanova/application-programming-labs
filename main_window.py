import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QLabel, QMessageBox, QPushButton, QVBoxLayout,
                             QHBoxLayout, QWidget)
from iterator import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """
        Функция создает главное окно приложения для просмотра изображений
        """
        super().__init__()
        self.setWindowTitle('Просмотр ')
        self.setGeometry(100, 100, 800, 600)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)


        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)


        self.button_layout = QHBoxLayout()


        self.load_annotation_button = QPushButton('Загрузить аннотацию')
        self.load_annotation_button.clicked.connect(self.load_annotation)
        self.button_layout.addWidget(self.load_annotation_button)


        self.next_image_button = QPushButton('Следующее изображение')
        self.next_image_button.clicked.connect(self.show_next_image)
        self.button_layout.addWidget(self.next_image_button)


        self.layout.addLayout(self.button_layout)


        self.image_iterator = None

    def load_annotation(self) -> None:
        """
        Функция загружает аннотацию
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл аннотации", options=options)
        if file_name:
            try:
                self.image_iterator = ImageIterator(file_name)
                QMessageBox.information(self, "Успех", "Файл аннотации загружен.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {str(e)}")

    def show_next_image(self) -> None:
        """
        Функция отображает следующее изображение
        """
        if self.image_iterator is None:
            QMessageBox.warning(self, "Предупреждение", "Сначала загрузите файл аннотации.")
            return
        try:

            image_path = next(self.image_iterator)
            self.display_image(image_path)
        except StopIteration:
            QMessageBox.information(self, "Информация", "Больше изображений нет.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить изображение: {str(e)}")


    def display_image(self, image_path) -> None:
        """
        Функция отображает изображение
        :param image_path: абсолютный путь к изображению
        :return: None
        """
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(600, 400, Qt.KeepAspectRatio))
            else:
                QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить изображение: {image_path}")
        else:
            QMessageBox.warning(self, "Ошибка", f"Файл не найден: {image_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
