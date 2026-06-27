import sys 
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QStackedLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime , Qt
from Stopwatch import Stopwatch_Page

class Alarm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
      
      
    def initUI(self):
        layout = QVBoxLayout()
        self.layout_setup = QStackedLayout()
        self.setLayout(self.layout_setup)
        self.front_page = QWidget()
        self.stopwatch_page = Stopwatch_Page()
        stopwatch_top_bar = QHBoxLayout()
        self.back_to_clock = QPushButton("Switch to digital clock", self.stopwatch_page)
        stopwatch_top_bar.addWidget(self.back_to_clock)
        self.stopwatch_page.stopwatch_layout.addLayout(stopwatch_top_bar)
        self.back_to_clock.clicked.connect(self.switch_clock)
        self.layout_setup.addWidget(self.front_page)
        self.layout_setup.addWidget(self.stopwatch_page)
        self.front_page.setLayout(layout)
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 500, 500)
        self.clock_text = QLabel()
        layout.addWidget(self.clock_text)
        self.TimerUpdating()
        self.DisplayedTime()
        self.clock_text.setStyleSheet("""
                               color: red;
                               background-color: black; 
                               font-family: Lucida Console;
                               font-size: 150px;
                            """)
        self.clock_text.setAlignment(Qt.AlignCenter)
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.switch_button = QPushButton("Switch to stopwatch", self )
        top_layout.addWidget(self.switch_button)
        self.switch_button.clicked.connect(self.switch_stopwatch)
        
       
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

    def switch_stopwatch(self):
        self.layout_setup.setCurrentIndex(1)
    
    def switch_clock(self):
        self.layout_setup.setCurrentIndex(0)



if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Alarm()
    window.show()
    sys.exit(application.exec_())