import string


def get_details_from_postal_code(postal_code: str) -> list:
    """When provided a postal code this function will return the province and the location rural or urban

    Args:
        postal_code (str): Valid 6 (or 7 with single space ex:A1E 5X0) character postal code

    Raises:
        TypeError: Happens if provided non String
        ValueError: Postal code to long
        ValueError: in 7 length postal code if 4th character is not a space
        ValueError: Incorrect length
        ValueError: Every even character must be a number
        ValueError: Every odd character must be a letter
        ValueError: Invalid first letter, which identifies province

    Returns:
        list: A liust with two entries, [Province,Region]
    """
    # Check if our type is correct
    if type(postal_code) != str:
        raise TypeError(f'{postal_code} is not a string')
    # Our max length is 7
    if len(postal_code) > 7:
        raise ValueError('Postal Code is to long!')
    # If our postal code is 7 characters long the fourth must be a space
    if len(postal_code) == 7 and postal_code[3] != ' ':
        raise ValueError('Incorrect Postal Code - Please use one (or no) spaces to seperate your postal code.')
    # We remove all spaces
    postal_code = postal_code.replace(' ', '')
    # Make sure its in the correct Format (All Uppercase)
    postal_code = postal_code.upper()
    # After removing the space we should be exactly 6 characters long
    if len(postal_code) != 6:
        raise ValueError(f'{postal_code} is invalid as it is not the correct length')
    counter = 1
    # We check if all the even characters are numbers
    for number in postal_code[1::2]:
        if number not in '1234567890':
            raise ValueError(
                f"{postal_code} is not a valid Postal Code. your {counter + 1} character - ({postal_code[counter]}) is not a valid number")
        counter += 2
    counter = 0
    # We check if all the odd characters are letters
    for letter in postal_code[0::2]:
        if letter not in string.ascii_uppercase:
            raise ValueError(
                f'{postal_code} is not a valid Postal Code. your {counter + 1} character - ({postal_code[counter]}) is not a valid letter')
        counter += 2
    # Confirm that the first letter is a valid region identifier
    if postal_code[0] not in 'ABCEGHJKLMNPRSTVXY':
        raise ValueError(f'{postal_code} is invalid, {postal_code[0]} is not a valid Region')
    return_list = []
    location = postal_code[1]
    province_dictionary = {'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick',
                           'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec', 'K': 'Ontario'
        , 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba', 'S': 'Saskatchewan',
                           'T': 'Alberta', 'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories',
                           'Y': 'Yukon', }
    return_list.append(province_dictionary[postal_code[0]])
    match location:
        case '0':
            return_list.append('rural')
        case _:
            return_list.append('urban')
    return return_list


if __name__ == "__main__":
    print("~~~Enter a postal to get its details~~~")
    # Keep trying until we get it right
    while True:
        try:
            user_postal_code = input('Enter a Postal Code: ')
            print(f'The details for {user_postal_code} are: {get_details_from_postal_code(user_postal_code)}')
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        # We shouldnt encounter any other errors, but if we do...
        except Exception as e:
            print(f'{type(e)} - {e}')
        else:
            break
