import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class FlowerClassificationApp(QWidget):

    def __init__(self):
        super().__init__()

        self.clf = svm.SVC(kernel='linear', C=1, probability=True)
        self.clf.fit(iris.data, iris.target)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.browse_button = QPushButton('Browse', self)
        self.browse_button.clicked.connect(self.browse_image)
        self.classify_button = QPushButton('Classify', self)
        self.classify_button.clicked.connect(self.classify_image)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.classify_button)

        self.setLayout(layout)

    def browse_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select an image", "", "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)", options=options)
        if file_path:
            pixmap = QPixmap(file_path)
            self.label.setPixmap(pixmap)

    def classify_image(self):
        pass