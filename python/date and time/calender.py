import calendar
import datetime

''' input containing the space separated month, day and year, respectively, in    format.'''

user_input = input()

#converts the string to date time object
date_o = datetime.datetime.strptime(user_input, '%m %d %Y')

#gets the day of the week
day_week = calendar.day_name[date_o.weekday()]
result = day_week.upper()

print(result)