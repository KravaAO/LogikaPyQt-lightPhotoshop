from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QListWidget,
                             QPushButton, QLabel, QFileDialog)
from PyQt5.QtGui import QPixmap
import os


folder_path = None


def open_folder():
    global folder_path
    try:
        # обираємо шлях до папки
        folder_path = QFileDialog.getExistingDirectory()
        # цикл по файлам з папки
        for file in os.listdir(folder_path):
            file_list.addItem(file)
    except Exception as e:
        print(e)


def show_image(file_name):
    global folder_path
    try:
        img = QPixmap(folder_path + '/' + file_name.text())
        img_label.setPixmap(img)
    except Exception as e:
        print(e)


app = QApplication([])
window = QWidget()
window.resize(1000, 700)

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
main_layout.addLayout(left_layout, 1)
right_layout = QVBoxLayout()
main_layout.addLayout(right_layout, 2)

# ліва частина екрана
file_list = QListWidget()
left_layout.addWidget(file_list)
load_btn = QPushButton('Завантажити папку')
left_layout.addWidget(load_btn)

# права частина екрана
img_label = QLabel('Тут буде твоє зображення')
right_layout.addWidget(img_label)
settings_img_layout = QHBoxLayout()
rotate_btn = QPushButton('Повернути зображення на 90')
settings_img_layout.addWidget(rotate_btn)
contrast_btn =QPushButton('Контраст')
settings_img_layout.addWidget(contrast_btn)
right_layout.addLayout(settings_img_layout)

# підключення кнопок до подій
load_btn.clicked.connect(open_folder)
file_list.itemClicked.connect(show_image)

window.setLayout(main_layout)
window.show()
app.exec()
