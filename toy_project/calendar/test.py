from datetime import datetime, timedelta
import calendar

myCalendar = calendar.Calendar()
myCalendar.setfirstweekday(calendar.SUNDAY)

# 한달 단위 보기
target_year = 2020
target_month = 1
print(myCalendar.monthdatescalendar(target_year, target_month))

# 주단위 보기
target_week = 1
print('')

print(myCalendar.monthdatescalendar(target_year, target_month)[target_week-1])
