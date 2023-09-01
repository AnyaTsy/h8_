from datetime import datetime, timedelta, date

def get_birthdays_per_week(users):
    today = date.today()
    current_year = today.year
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    next_monday = monday + timedelta(weeks=1)
    
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    birthdays = {}
    for user in users:
        name = user['name']
        bday = user['birthday']
        if isinstance(bday, datetime):
            bday = bday.date()
        
        # Перевірка, чи день народження випадає на вихідний
        if bday.weekday() >= 5:  # 5 - субота, 6 - неділя
            weekday = 'Monday'  # Переносимо на понеділок
        else:
            weekday = weekdays[bday.weekday()]
        
        if bday >= monday and bday <= sunday:
            if weekday not in birthdays:
                birthdays[weekday] = []
            birthdays[weekday].append(name)
        
             
    return birthdays
