def duration_in_seconds(days: int, hours: int, minutes: int, seconds: float):
    assert type(days) == int, '(days) must be an int'
    assert type(hours) == int, '(hours) must be an int'
    assert type(minutes) == int, '(minutes) must be a int'
    assert type(seconds) == float, '(seconds) must be a float'
    if 0 > hours or hours > 24:
        raise ValueError('Hours must be greater than 0 and less than 24')
    if 0 > minutes or minutes > 59:
        raise ValueError('Minutes must be greater than 0 and less than 60')
    if 0 > seconds or seconds > 59:
        raise ValueError('Seconds must be greater than 0 and less than 60')
    return (days * 86400) + (hours * 3600) + (minutes * 60) + seconds


if __name__ == "__main__":
    while True:
        try:
            user_days = int(input('Enter days: '))
            user_hours = int(input('Enter hours: '))
            user_minutes = int(input('Enter minutes: '))
            user_seconds = float(input('Enter seconds: '))
            time = duration_in_seconds(user_days, user_hours, user_minutes, user_seconds)
        except ValueError as ve:
            print(ve)
        else:
            print(
                f'The time of {user_days} days, {user_hours} hours, {user_minutes} minutes, and {user_seconds} seconds is exactly {time} seconds')
            break
