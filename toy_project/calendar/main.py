from datetime import datetime, timedelta
import calendar

myCalendar = calendar.Calendar()

#print(myCalendar.yeardatescalendar(2020))

# 한달 단위 보기
# myCalendar.setfirstweekday(calendar.SUNDAY)
# print('=======itermonthdates=======')
# for day in myCalendar.itermonthdates(2020,1):
#     print(day.year, day.month, day.day, day.weekday())

# 주단위 보기
target_week = 2
myCalendar.setfirstweekday(calendar.SUNDAY)

for day in myCalendar.itermonthdates(2020,1):
    if day.isocalendar()[1] is target_week:
        print(day.year, day.month, day.day, day.weekday())

# print('=======itermonthdays=======')
# for day in myCalendar.itermonthdays(2020,1):
#     print(day)

# print('=======itermonthdays2=======')
# for day in myCalendar.itermonthdays2(2020,1):
#     print(day)

# print('=======itermonthdays3=======')
# for day in myCalendar.itermonthdays3(2020,1):
#     print(day)

# print('=======itermonthdays4=======')
# for day in myCalendar.itermonthdays4(2020,1):
#     print(day)

