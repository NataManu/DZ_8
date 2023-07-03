from datetime import datetime, timedelta
from collections import defaultdict


employees = [{"name": "Dmitro", "birthdate": datetime( 1981, 4,23)},
            {"name": "Olena", "birthdate": datetime( 1995, 7, 12)},
            {"name": "Alex", "birthdate": datetime( 1972, 7, 14)},
            {"name": "Serg", "birthdate": datetime( 1978, 7, 10)},
            {"name": "Olga", "birthdate": datetime( 1998, 7, 8)},
            {"name": "Roman", "birthdate": "30.12.2007"}]


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5-current_date.weekday())
    return start_period.date(), (start_period+timedelta(6)).date()


def get_birthdays_per_week(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for employee in list_of_emp:
        bd = employee["birthdate"]
        if isinstance(bd,datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        bd = bd.replace(year=current_year)   

        start, end = get_period()
        if start <= bd <= end:
            if bd.weekday() in (5,6):
                result["Monday"].append(employee["name"])
            else:
                result[bd.strftime("%A")].append(employee["name"])
    
    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for k in week_list:
        if result[k] != []: 
            print (k,':',", ".join(result[k]))
    return result


if __name__ =="__main__":
    get_birthdays_per_week(employees)
    