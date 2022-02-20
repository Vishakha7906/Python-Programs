import calendar
from datetime import date
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
 
    message: explanation of the error.
 
    """
    def __init__(self, message):
        self.message = message
def meetup(year, month, week, day_of_week):
    num_of_days_in_month = calendar.monthrange(year, month)[1]
    days = {}
    for day in range(1, num_of_days_in_month + 1):
        weekday_name = calendar.day_name[date(year, month, day).weekday()] 
        if weekday_name not in days:
            days[weekday_name] = []
        days[weekday_name].append(day)
    day_of_month = None
    if week in ['1st', '2nd', '3rd', '4th', '5th']:
        week_int = int(week[0])
        if len(days[day_of_week]) >= week_int:
            day_of_month = days[day_of_week][week_int - 1]
    if week is 'last':
        day_of_month = days[day_of_week][-1]
    if week is 'teenth':
        day_of_month = list(filter(lambda x: 12 < x < 20, days[day_of_week]))[0]
    if day_of_month is None:
        raise MeetupDayException('That day does not exist.')
        
    return date(year, month, day_of_month)