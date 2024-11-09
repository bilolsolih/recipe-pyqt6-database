import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog


class ImageFileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image File Manager")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.image_label = QLabel("No image selected")
        self.layout.addWidget(self.image_label)

        self.browse_button = QPushButton("Browse for Image")
        self.browse_button.clicked.connect(self.browse_image)
        self.layout.addWidget(self.browse_button)

        self.move_button = QPushButton("Move Image")
        self.move_button.clicked.connect(self.move_image)
        self.layout.addWidget(self.move_button)

        self.setLayout(self.layout)

        self.selected_image_path = None

    def browse_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)")
        if file_name:
            self.selected_image_path = file_name
            self.display_image(file_name)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(400, 400, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))

    def move_image(self):
        if not self.selected_image_path:
            return

        destination_folder = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if destination_folder:
            file_name = os.path.basename(self.selected_image_path)
            new_path = os.path.join(destination_folder, file_name)
            os.rename(self.selected_image_path, new_path)
            self.image_label.setText(f"Moved to: {new_path}")
            self.selected_image_path = None
            self.image_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFileManager()
    window.show()
    sys.exit(app.exec())
