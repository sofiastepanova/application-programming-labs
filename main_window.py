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
        self.setWindowTitle('Просмотр ежиков ')
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
        Загружает аннотацию из выбранного файла.
        """
        file_name = self._select_annotation_file()
        if file_name:
            self._process_annotation_file(file_name)

    def _select_annotation_file(self) -> str:
        """
        Открывает диалог выбора файла и возвращает путь к выбранному файлу.

        :return: Путь к файлу аннотации или пустая строка, если файл не выбран.
        """
        options = QFileDialog.Options()
        return QFileDialog.getOpenFileName(self, "Выберите файл аннотации", options=options)[0]

    def _process_annotation_file(self, file_name: str) -> None:
        """
        Обрабатывает файл аннотации и загружает его.

        :param file_name: Путь к файлу аннотации.
        """
        try:
            self.image_iterator = ImageIterator(file_name)
            QMessageBox.information(self, "Успех", "Файл аннотации загружен.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {str(e)}")


    def show_next_image(self):
        """
        Функция отвечает за отображение следующего изображения из выбранного набора данных.
        """
        if self.image_iterator is None:
            self.image_label.setText("Сначала загрузите аннотацию")
            return

        try:
            image_path = next(self.image_iterator)
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(
                pixmap.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio,
                )
            )
        except StopIteration:
            self.image_label.setText("больше ежиков нет")

    def display_image(self, image_path: str) -> None:
        """
        Отображает изображение в виджете.

        :param image_path: абсолютный путь к изображению
        """
        try:
            if not os.path.isfile(image_path):
                raise FileNotFoundError(f"Файл не найден: {image_path}")

            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                raise RuntimeError(f"Не удалось загрузить изображение: {image_path}")

            scaled_pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)

        except (FileNotFoundError, RuntimeError) as e:
            QMessageBox.warning(self, "Ошибка", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
