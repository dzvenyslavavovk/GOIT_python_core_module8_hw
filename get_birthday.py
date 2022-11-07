from datetime import date
from datetime import datetime,timedelta
def get_birthdays_per_week(users):
    days=[]
    birthdays={}
    start_date=datetime.now()
    end_date=start_date+timedelta(days=7)
    days_name = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
        }
    for user in users:
        user['birthday'] = user['birthday'].replace(year=start_date.year)
        day = days_name.get(user['birthday'].weekday())
        if day=='Saturday' or day=='Sunday':
            day='Monday'
        if day not in days:
            days.append(day)
        if start_date<=user['birthday']<=end_date:
            if day not in birthdays:
                birthdays[day]=[user['name']]
            else:
                birthdays[day].append(user['name'])
    for day in birthdays.keys():
        result = f'{day}: '
        for name in birthdays[day]:
            result += f'{name}, '
        print(f'{result[:-2]}')

users=[    
    {'name': 'Yurii', 'birthday': datetime(1990, 11, 15)}, 
    {'name': 'Daria', 'birthday': datetime(1995, 11, 8)},
    {'name': 'Roman', 'birthday': datetime(1990, 4, 2)},
    {'name': 'Oleksandr', 'birthday': datetime(1992, 11, 7)},
    {'name': 'Iryna', 'birthday': datetime(1998, 11, 11)}, 
    {'name': 'Sofiia', 'birthday': datetime(1998, 11, 14)} 
    ]
    
get_birthdays_per_week(users)