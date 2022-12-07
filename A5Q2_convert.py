def convert_feet_and_inches_to_meters(feet:int, inches) ->float:
    if type(feet) != int:
        raise TypeError('feet must be an int')
    if type(inches) not in [int,float]:
        raise TypeError('inches must be a int or float')
    if inches < 0:
        raise ValueError('inches must be greater than 0')
    if inches >= 12:
        raise ValueError('inches must be less than 12')
    meters = (feet * 0.3048) + (inches * 0.0254)
    return meters

if __name__ == "__main__":
    while True:
        try:
            user_feet = int(input("Enter feet: "))
            user_inches = float(input("Enter inches: "))
            user_length = convert_feet_and_inches_to_meters(user_feet, user_inches)
        except ValueError as ve:
            print('Encountered an error:')
            print(ve)
        except TypeError as te:
            print('Encountered an error:')
            print(ve)
        else:
            print(f"Your length in meters from {user_feet}, and {user_inches} is {user_length}")
            break

