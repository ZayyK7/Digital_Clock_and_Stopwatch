import sys 
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel
from PyQt5.QtCore import QTimer, QTime , Qt

class Alarm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
      
      
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(0, 0, 500, 500)
        self.clock_text = QLabel(self)
        self.TimerUpdating()
        self.DisplayedTime()
    
    def TimerUpdating(self):
        self.Timer = QTimer(self)
        self.Timer.timeout.connect(self.DisplayedTime)
        self.Timer.start(1000)

    def DisplayedTime(self):
          self.clock_text.setText(QTime.currentTime().toString("hh:mm:ss"))



if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Alarm()
    window.show()
    sys.exit(application.exec_())