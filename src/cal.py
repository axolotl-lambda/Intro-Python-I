"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
import datetime


month, year = [(lambda x: int(x) if x.isdigit() else False)(x) for x in (input(
    "Enter numbers: ") + ' x x').split(' ')[:2]]

if not month:
    month = datetime.date.today().month

if not year:
    year = datetime.date.today().year

print(month)
print(year)

months = {0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May', 5: 'Jun',
          6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov', 11: 'Dec'}

cal = calendar.monthcalendar(year, month)

print('|+++++ %s %s +++++|' % (months[month], year))
print('|Su Mo Tu We Th Fr Sa|')
print('|--------------------|')

border = '|'
for week in cal:
    line = border

    for day in week:
        if day == 0:
            line += '   '  # 3 spaces for blank days
        elif len(str(day)) == 1:
            line += ' %d ' % day
        else:
            line += '%d ' % day

    line = line[0:len(line) - 1]  # remove space in last column
    line += border
    print(line)

print('|--------------------|\n')
