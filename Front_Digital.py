import sys 
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime , Qt

class Alarm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
      
      
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 500, 500)
        self.clock_text = QLabel(self)
        self.TimerUpdating()
        self.DisplayedTime()
        self.clock_text.setStyleSheet("""
                               color: red;
                               background-color: black; 
                               font-family: Lucida Console;
                               font-size: 150px;
                            """)
        layout = QVBoxLayout()
        layout.addWidget(self.clock_text)
        self.setLayout(layout)
        self.clock_text.setAlignment(Qt.AlignCenter)
    
    def TimerUpdating(self):
        self.Timer = QTimer(self)
        self.Timer.timeout.connect(self.DisplayedTime)
        self.Timer.start(1000)

    def DisplayedTime(self):
          self.clock_text.setText(QTime.currentTime().toString("hh:mm:ss"))

    def resizeEvent(self, event):
        IntegerFontSize = self.width()//6
        font = self.clock_text.font()
        font.setPixelSize(IntegerFontSize)
        self.clock_text.setFont(font)
        super().resizeEvent(event)




if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Alarm()
    window.show()
    sys.exit(application.exec_())