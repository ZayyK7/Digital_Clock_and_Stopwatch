import sys 
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QStackedLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime , Qt

class Stopwatch_Page(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
      
      
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.stopwatch_layout = QVBoxLayout()
        self.stopwatch_text = QLabel("00:00:00", self)
        self.stopwatch_text.setAlignment(Qt.AlignCenter)
        self.stopwatch_layout.addWidget(self.stopwatch_text)
        self.Stopwatch_Buttons(self.stopwatch_layout)
        self.setLayout(self.stopwatch_layout)
        self.stopwatch_text.setStyleSheet("""                         
                                           color: yellow;
                                           font-size: 150px;
                                           background-color: grey;
                                          """)                        # Setting the style of the stopwatch
        self.Update_time = 0                                        # Declaring the term to be updated consistently in the stopwatch
        self.Stopwatch_Timer()
        

    def Stopwatch_Timer(self):
        self.stopwatch_timer = QTimer()
        self.stopwatch_timer.timeout.connect(self.Update_Stopwatch)

    def Update_Stopwatch(self):
        self.Update_time = self.Update_time + 1                     # Updating the term by 1 second
        Hours = self.Update_time // 3600                            # Calculation for the hours minutes and seconds
        Minutes = (self.Update_time % 3600) // 60
        Seconds = self.Update_time % 60
        total_time = (f"{Hours:02d}:{Minutes:02d}:{Seconds:02d}")       # Text formatted to standard stopwatch form
        self.stopwatch_text.setText(total_time)
        
    def Stopwatch_Buttons(self, layout:QVBoxLayout):
        self.StartButton = QPushButton("Start Timer", self)          # Declaring the three buttons for a stopwatch
        self.PauseButton = QPushButton("Pause Timer", self)
        self.ResetButton = QPushButton("Reset Timer", self)
        button_layout = QHBoxLayout()                                # Declaring a new row for those three buttons
        button_layout.addWidget(self.StartButton)
        button_layout.addWidget(self.PauseButton)
        button_layout.addWidget(self.ResetButton)
        layout.addLayout(button_layout)
        self.StartButton.clicked.connect(self.Button_Output)
        self.PauseButton.clicked.connect(self.Button_Output)
        self.ResetButton.clicked.connect(self.Button_Output)

    def Button_Output(self):                                        # Gives the buttons their outputs
        choice = self.sender()
        if choice == self.StartButton:
            self.stopwatch_timer.start(1000)
        elif choice == self.PauseButton:
            self.stopwatch_timer.stop()
        elif choice == self.ResetButton:
            self.stopwatch_timer.stop()
            self.Update_time = 0
            self.stopwatch_text.setText("00:00:00")




if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Stopwatch_Page()
    window.show()
    sys.exit(application.exec_())