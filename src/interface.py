import sys 
from PyQt5.QtWidgets import QApplication, QWidget

class octoPilot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("OctoPilot")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = octoPilot()
    sys.exit(app.exec_())