from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QLabel


class TopNavigationBar(QWidget):
    def __init__(self):
        super().__init__()
        top_bar_layout = QHBoxLayout()
        top_bar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        top_right_layout = QHBoxLayout()

        back_button = QLabel()
        back_button.setPixmap(QPixmap('assets/back-arrow.svg'))

        menu_title = QLabel('Categories')
        menu_title.setStyleSheet("color: #FD5D69; font-weight: bold; font-size: 20px;")

        notifications_button = QLabel()
        notifications_button.setPixmap(QPixmap('assets/notification-button.svg'))

        search_button = QLabel()
        search_button.setPixmap(QPixmap('assets/search-button.svg'))

        top_right_layout.addWidget(notifications_button)
        top_right_layout.addWidget(search_button)

        top_right_widget = QWidget()
        top_right_widget.setLayout(top_right_layout)

        top_bar_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        top_bar_layout.addWidget(menu_title, alignment=Qt.AlignmentFlag.AlignCenter)
        top_bar_layout.addWidget(top_right_widget, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(top_bar_layout)
