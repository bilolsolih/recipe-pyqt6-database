import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


def check_file_exists(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File at {path} doesn't exist!")


def create_image_label(path: str, width: float, height: float) -> QLabel:
    check_file_exists(path)
    image_pixmap = QPixmap(path)
    image_label = QLabel()
    image_label.setPixmap(image_pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio))
    image_label.setFixedSize(width, height)
    return image_label
