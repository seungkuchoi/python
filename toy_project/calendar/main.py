import sys

from PyQt5.QtWidgets import QApplication
from MyCalendar import MyCalendar

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MyCalendar()
    main_widget.show()
    exit(app.exec_())