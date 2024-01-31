from datetime import datetime


def median(list):

    n = len(list)

    if n == 0:
        return None

    sorted_list = sorted(list)
    middle_index = n // 2

    if n % 2 == 0:
        return (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2.0
    else:
        return sorted_list[middle_index]    


def get_median_of_first_week_expenses(expenses):
    result = None
    week_expenses = []

    for month, days in expenses.items():        # iteracja po elementach (data i dane dla danego dnia)
        month_first_day = datetime.strptime(month, "%Y-%m").replace(day=1)
        first_day_number = month_first_day.weekday()
        sorted_days = sorted(days.keys())       # posortowane numery dni z dancyh 
        
        
        for day in sorted_days:                 # iteracja przez posortowane dni
            if days[day] and int(day) <= 7-first_day_number:        # jeśli dzień nie jest pusty- są wydatki to                    
                    day_expenses = [expense for category in days[day].values() for expense in category]
                    week_expenses.extend(day_expenses)
                    print(week_expenses)

    print(week_expenses)
    print(sorted(week_expenses))                
    result = median(week_expenses)
    return result

# Przykładowe dane
expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}

print(get_median_of_first_week_expenses(expenses))
