import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PIL import Image, ImageDraw, ImageFont
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt


class WatermarkApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My watermark script")
        self.setGeometry(100, 100, 800, 800)

        # Create a label to display the selected image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("QLabel { background-color: white; }")

        # Create a layout and set it as the central widget
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Create a button to open the file dialog
        self.upload_button = QPushButton("Upload Image", self)
        self.upload_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.upload_button)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)",
                                                   options=options)
        if file_name:
            self.add_watermark(file_name)

    def add_watermark(self, image_path):
        image = Image.open(image_path)

        # Add your watermark text or logo here
        watermark_text = "Sensual❤️"
        font = ImageFont.truetype("arial.ttf", 60)
        watermark_color = (255, 0, 0)  # Red color

        # Create a transparent overlay with the same size as the image
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))

        # Draw the watermark text on the overlay
        draw = ImageDraw.Draw(overlay)
        text_width, text_height = draw.textsize(watermark_text, font)
        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2
        draw.text((x, y), watermark_text, font=font, fill=watermark_color)

        # Apply the overlay to the image
        watermarked_image = Image.alpha_composite(image.convert("RGBA"), overlay)

        # Display the watermarked image
        self.image_label.setPixmap(watermarked_image.toqpixmap())

    def show(self):
        super().show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    watermark_app = WatermarkApp()
    watermark_app.show()
    sys.exit(app.exec_())
