
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

from datetime import datetime
from calendar import Calendar

from functools import partial

class UserData():
    """
    This class is responsible for extracting user data from 'setting.json'
    """
    def __init__(self, user_file):
        import json
        with open(user_file) as file:
            self._json_object = json.load(file)
            self.date_type = self._json_object["viewType"]
            self.first_weekday = self._get_weekday_index()

    def _get_weekday_index(self):
        weekday_list = ['monday','tuesday', 'wednesday', \
                        'thusday', 'friday', 'saturday', 'sunday']
        for index, weekday in enumerate(weekday_list):
            if weekday == self._json_object["firstWeekday"]:
                return index

    def write(self, key, value):
        self._json_object[key] = value

class DateInfo(Calendar):
    def __init__(self, first_weekday = 0):
        self.setfirstweekday(first_weekday)

        today = datetime.today()
        self.year = today.year
        self.month = today.month
        self.day = today.day
        self.week = today.isocalendar()[1] % 5

    def get_dates(self, date_type):
        self.date_type = date_type
        if date_type == 'monthly':
            return self.monthdatescalendar(self.year, self.month)
        else:
            return self.monthdatescalendar(self.year, self.month)[self.week]

class Scheduler(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        self.setGeometry(800, 400, 300, 150)
        textLabel = QPushButton("scheduler", self)
        textLabel.move(20, 20)

class MyCalendar(QWidget):
    def __init__(self):
        self.user_data = UserData('settings.json')
        self.date_info = DateInfo(self.user_data.first_weekday)
        self.scheduler = Scheduler()
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Seungku 캘린더")
        layout = QGridLayout()
        self.setLayout(layout)

        col, row = 7, 5
        if self.user_data.date_type == 'weekly':
            row = 1

        for x in range(0, row):
            for y in range(0, col):
                day = self.date_info.get_dates(self.user_data.date_type)[x][y].day
                date_button = QPushButton(str(day), self)
                date_button.clicked.connect(partial(self.show_scheduler, date_button))
                layout.addWidget(date_button, x, y)

    def show_scheduler(self, button):
        button.setStyleSheet("background-color: red")
        self.scheduler.show()
