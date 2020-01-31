
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from datetime import datetime
from calendar import Calendar

class _UserData():
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

class _DateInfo(Calendar):
    def __init__(self):
        self._user_data = _UserData('settings.json')
        self.setfirstweekday(self._user_data.first_weekday)

        today = datetime.today()
        self.year = today.year
        self.month = today.month
        self.day = today.day
        self.week = 0

        date_list = self.monthdatescalendar(self.year, self.month)
        if self._user_data.view_type == 'monthly':
            self.date_list = date_list
        else:
            self.date_list = date_list[self.week]

    def show(self):
        for index, date in enumerate(self.date_list):
            print(index, date)

class MyCalendar(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.date_info = _DateInfo()
        self.date_info.show()

    def init_widget(self):
        self.setWindowTitle("Seungku 캘린더")