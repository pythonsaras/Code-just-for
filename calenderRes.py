from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import*
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting  title
        self.setWindowTitle("Calender")
        # setting geometry
        self.setGeometry(100,100,600,400)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()
    # define method UiComponents
    def UiComponents(self):
        # creating a QCalenderWidget object
        calender=QCalendarWidget(self)
        # setting gm for calender
        calender.setGeometry(10,10,400,250)
        # create push button 
        push=QPushButton("next year",self)
        # geometry to push
        push.setGeometry(120,280,100,40)
        # adding action to push
        push.clicked.connect(lambda:do_action())

        def do_action():
            # showing next year
            calender.showNextYear()


        
# create pyqt5 app
App=QApplication(sys.argv)
# create instance of our window
window=Window()
# start app 
sys.exit(App.exec())