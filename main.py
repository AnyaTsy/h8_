from datetime import datetime, timedelta, date

def get_birthdays_per_week(users):
    today = date.today()
    monday = today 
    sunday = monday + timedelta(days=6)
    current_year = today.year
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    birthdays = {}
    for user in users:
        name = user['name']
        bday = user['birthday']
        bday = bday.replace(year=current_year)
        if bday < monday:
            bday = bday.replace(year=current_year+1)
        
        # Перевірка, чи день народження випадає на вихідний
        if bday.weekday() >= 5:  # 5 - субота, 6 - неділя
            weekday = 'Monday'  # Переносимо на понеділок
        else:
            weekday = weekdays[bday.weekday()]
        
        if bday >= monday and bday <= sunday:
            if weekday not in birthdays:
                birthdays[weekday] = []
            birthdays[weekday].append(name)
            
        
    print(birthdays)        
    return birthdays
