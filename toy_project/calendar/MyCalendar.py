
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from datetime import datetime
import calendar

class MyCalendar(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.initCalendar()
        self.initWidget()

        self.showDate()

    def __loadSettings(self):
        import json
        with open('settings.json') as setting_file:
            json_object = json.load(setting_file)
            self.viewType = json_object["viewType"]
            self.firstWeekDay = json_object["firstWeekDay"]

    def initCalendar(self):
        self.__loadSettings()

        myCalendar = calendar.Calendar()
        myCalendar.setfirstweekday(calendar.SUNDAY)
        today = datetime.today()

        self.dateList = myCalendar.monthdatescalendar(today.year, today.month)

    def showDate(self):
        '''
        test method
        '''
        if self.viewType == 'Weekly':
            print(self.dateList)
        else:
            print(self.dateList[1]) # index means target week

    def initWidget(self):
        self.setWindowTitle("Seungku 캘린더")