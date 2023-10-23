import math
import calendar

expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        },
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

def get_first_sunday(year, month):
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        Sunday = week[6]
        if Sunday != 0:
            return Sunday


def get_median_of_first_week_expenses(expenses):
    first_month_week_expenses = []
    for data, days_in_month in expenses.items():
        year, month = map(int, data.split('-'))
        first_sunday = get_first_sunday(year, month)
        if first_sunday:
            for days, categories in days_in_month.items():
                day = int(days)
                if day <= first_sunday:
                    for value in categories.values():
                        if value:
                            for values in value:
                                first_month_week_expenses.append(values)
    if not first_month_week_expenses:
        return "Brak wartości"
    else:
        first_month_week_expenses.sort()
        mid = len(first_month_week_expenses) // 2
        if len(first_month_week_expenses) % 2 == 0:
            return (first_month_week_expenses[mid - 1] + first_month_week_expenses[mid]) / 2
        else:
            return first_month_week_expenses[mid]


print(f"Mediana wydatków wykonanych do pierwszej niedzieli miesiąca włącznie wynosi: {get_median_of_first_week_expenses(expenses)}")
