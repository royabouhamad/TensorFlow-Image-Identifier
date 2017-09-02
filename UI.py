import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tensor.label_image import *

class Identifier(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()
    def initUI(self):
        self.line = QLabel(self)
        self.line = QLabel(self)
        self.line.move(5, 550)
        self.line.resize(400, 40)
        self.line.show()

        browse = QPushButton("Browse...", self)
        browse.move(400, 555)
        browse.resize(100, 40)
        browse.clicked.connect(self.openImage)

        self.label = QLabel(self)
        self.label.resize(500, 500)
        self.label.setPixmap(QPixmap('images/NoImage.jpg').scaled(self.width(), self.height(), Qt.KeepAspectRatio))
        self.label.show()

        self.setGeometry(300, 300, 500, 600)
        self.setWindowTitle("Image Identifier")
        self.setFixedSize(500, 600)
        self.show()

    def openImage(self):
        fName = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.jpg *.jpeg)')
        try:
            filePath = fName[0]
            human_string, score = label(filePath)
            self.line.setText(human_string + " " + str(round(score, 2)) + "%")
            self.label.setPixmap(QPixmap(filePath).scaled(self.width(), self.height(), Qt.KeepAspectRatio))
        except:
            self.label.setPixmap(QPixmap('images/NoImage.jpg').scaled(self.width(), self.height(), Qt.KeepAspectRatio))
            self.line.setText("No image selected!")

def main():
    app = QApplication(sys.argv)
    main = Identifier()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
