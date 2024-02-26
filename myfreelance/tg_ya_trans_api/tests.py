from django.test import TestCase

# Create your tests here.
from datetime import date, time
import datetime
print(date.today())
print(time(12,21))

my_time_string = "01:20"
my_datetime = datetime.datetime.strptime(my_time_string, "%H:%M").time()
print(my_datetime)
print(type(my_datetime))
assert my_datetime.hour == 12