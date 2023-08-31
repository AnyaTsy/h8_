from datetime import datetime, timedelta, date
from collections import defaultdict

def get_period() -> tuple[date, date]:
    current_date = date.today()
    start_period = current_date + timedelta(days=5 - current_date.weekday())
    return start_period, start_period + timedelta(6)

def get_birthdays_per_week(users):
    result = defaultdict(list)
    current_year = date.today().year

    for employee in users:
        bd = employee["birthday"]
        if isinstance(bd, datetime.date):
            bd = bd.date()
        elif isinstance(bd, datetime.date):
            bd = bd
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()

        bd = bd.replace(year=current_year)
        start, end = get_period()

        if start <= bd <= end:
            weekday = bd.strftime("%A")
            if bd.weekday() in (5, 6):
                weekday = "Monday"
            result[weekday].append(employee["name"])

    return result

if __name__ == "__main__":
    employees = [
        {"name": "Pitier", "birthday": datetime(1990, 6, 28)},
        {"name": "Angel", "birthday": "24.06.2000"},
        {"name": "Angel", "birthday": datetime(1985, 6, 28)}
    ]

    for key, value in get_birthdays_per_week(employees).items():
        print(key, value)
