
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

from datetime import datetime
from calendar import Calendar

class UserData():
    """
    This class is responsible for extracting user data from 'setting.json'
    """
    def __init__(self, user_file):
        import json
        with open(user_file) as file:
            self._json_object = json.load(file)
            self.view_type = self._json_object["viewType"]
            self.first_weekday = self._get_weekday_index()

    def _get_weekday_index(self):
        weekday_list = ['monday','tuesday', 'wednesday', \
                        'thusday', 'friday', 'saturday', 'sunday']
        for index, weekday in enumerate(weekday_list):
            if weekday == self._json_object["firstWeekday"]:
                return index

    def write(self, key, value):
        self._json_object[key] = value

user_data = UserData('settings.json')

class DateInfo(Calendar):
    def __init__(self):
        self.setfirstweekday(user_data.first_weekday)

        today = datetime.today()
        self.year = today.year
        self.month = today.month
        self.day = today.day
        self.week = today.isocalendar()[1] % 5

    def get_dates(self):
        if user_data.view_type == 'monthly':
            return self.monthdatescalendar(self.year, self.month)
        else:
            return self.monthdatescalendar(self.year, self.month)[self.week]

    def show(self):
        print(self.get_dates())

date_info = DateInfo()
#date_info.show()

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
        self.scheduler = Scheduler()
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Seungku 캘린더")
        layout = QGridLayout()
        self.setLayout(layout)

        row = 5
        col = 7

        for x in range(0, row):
            for y in range(0,col):
                date_button = QPushButton(str(date_info.get_dates()[x][y].day), self)
                date_button.clicked.connect(self.show_scheduler)
                layout.addWidget(date_button, x, y)

    def show_scheduler(self):
        self.scheduler.show()

