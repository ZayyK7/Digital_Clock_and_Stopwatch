import sys 
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel
from PyQt5.QtCore import QTimer, QTime 

class Alarm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
      
      
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(0, 0, 500, 500)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Alarm()
    window.show()
    sys.exit(application.exec_())