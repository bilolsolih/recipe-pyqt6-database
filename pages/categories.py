from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QScrollArea

from utils.db import create_connection, execute_read_query
from widgets.category import CategoryItem


class CategoriesPage(QScrollArea):
    def __init__(self, columns: int = 2):
        super().__init__()
        self.columns = columns
        self.widget = QWidget()
        self.connection = create_connection()

        self.__set_up_layout()
        self.setWidget(self.widget)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setStyleSheet("border: null;")

    def get_items(self) -> list[QWidget]:
        result = execute_read_query(self.connection, "SELECT category_name as name, photo from category;")
        items = []
        for item in result:
            items.append(CategoryItem(item["name"], item["photo"], 160, 145))

        return items

    def get_item_main(self) -> QWidget:
        return CategoryItem("Seafood", "assets/seafood.png", 356, 149, reverse_title_and_photo=True)

    def __set_up_layout(self) -> None:
        layout = QGridLayout()
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        column_index = 0
        row_index = 0

        for item in self.get_items():
            layout.addWidget(item, row_index, column_index)
            column_index += 1
            if column_index >= self.columns:
                row_index += 1
                column_index = 0

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.get_item_main())
        main_layout.addLayout(layout)

        self.widget.setLayout(main_layout)
