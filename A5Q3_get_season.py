def get_season(month: str, day: int) -> str:
    assert type(month) == str, 'month must be a string!'
    assert type(day) == int, 'day must be an int!'
    month = month.title()
    if month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October','November','December']:
        raise ValueError(f'{month} is not a valid month')
    if day > 31:
        raise ValueError('You cant have more than 31 days in a month')
    if day <= 0:
        raise ValueError('You cant have less than 0 days in a month')
    match month:
        case 'February':
            if day > 29:
                raise ValueError(f'{day} is too many days for month: {month}')
        case 'September'|'April'|'June'|'November':
            if day > 30:
                raise ValueError(f'{day} is too many days for month: {month}')
        case 'January'|'March'|'May'|'July'|'August'|'October'|'December':
            if day > 31:
                raise ValueError(f'{day} is too many days for month: {month}')
    match month:
        case "March" | "April" | "May" | "June":
            if month == "March" and day >= 20:
                return "Spring"
            elif month == "March" and day < 20:
                return "Winter"
            elif month == "June" and day <= 20:
                return "Spring"
            elif month == "June" and day >= 21:
                return "Summer"
            else:
                return "Spring"
        case  "July" | "August" | "September":
            if month == "September" and day <= 21:
                return "Summer"
            elif month == "September" and day >= 22:
                return "Fall"
            else:
                return "Summer"
        case "October"| "November" | "December":
            if month == "December" and day <= 20:
                return "Fall"
            elif month == "December" and day >= 21:
                return "Winter"
            else:
                return "Fall"
        case "January" | "February":
            return "Winter"


if __name__ == "__main__":
    while True:
        try:
            user_month = input("Enter the month: ")
            user_day = int(input("Enter the day: "))
            season = get_season(user_month, user_day)
        except ValueError as ve:
            print('Encounter an error:')
            print(ve)
        except TypeError as te:
            print('Encounter an error:')
            print(te)
        except Exception as e:
            print('Encounter an unexpected error:')
            print(f'{type(e)} - {e}')
        else:
            print(f"The season is {season}")
            break