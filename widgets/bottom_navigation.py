from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout


class BottomNavigationBarItem(QWidget):
    def __init__(self, photo: str):
        super().__init__()
        icon = QPixmap(photo)
        label = QLabel()
        label.setPixmap(icon.scaled(icon.width(), icon.height(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


class BottomNavigationBar(QWidget):
    def __init__(self):
        super().__init__()
        item1 = BottomNavigationBarItem("assets/home.svg")
        item2 = BottomNavigationBarItem("assets/chat.svg")
        item3 = BottomNavigationBarItem("assets/categories.svg")
        item4 = BottomNavigationBarItem("assets/profile.svg")

        self.setFixedWidth(256)
        self.layout = QHBoxLayout()
        self.layout.addWidget(item1)
        self.layout.addWidget(item2)
        self.layout.addWidget(item3)
        self.layout.addWidget(item4)

        self.tmp_widget = QWidget()
        self.tmp_widget.setLayout(self.layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tmp_widget)
        self.setLayout(self.main_layout)
        self.setStyleSheet("background-color: #FD5D69; border-radius: 30px;")
