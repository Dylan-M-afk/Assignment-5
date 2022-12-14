def calculate_gpa(book: dict) -> float:
    """Calculates gpa using CNA standard, when provided a correctly formatted dictionary

    Args:
        book (dict): book must be a valid gradebook formatted as {Course:{'Credit':creditvalueint,'score':scorevalueint}}

    Raises:
        ValueError: If the course detail dictionary has key values pairs that are not credit and score
        AssertionError: Invalid types

    Returns:
        float: The total points divided by the total points attempted
    """
    # Begin exception handling
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Confirm We have the right type
    assert type(book) == dict
    # Make sure the outer dict has str:dict pairs
    for key, values in book.items():
        assert type(key) == str
        assert type(values) == dict
    # Make sure the sub dicts values are all ints
    for sub_dict in book.values():
        for value in sub_dict.values():
            assert type(value) == int
    # Check for extra values
    for sub_dict in book.values():
        for key in sub_dict.keys():
            if key not in ['credit', 'score']:
                raise ValueError('Invalid key value pair in course information')
    # End exception handling
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    grade_values = []
    # Get the grade value from score
    for details in book.values():
        if details['score'] >= 80:
            grade_values.append(4)
        elif details['score'] in [70, 75]:
            grade_values.append(3)
        elif details['score'] in [60, 65]:
            grade_values.append(2)
        elif details['score'] in [50, 55]:
            grade_values.append(1)
        elif details['score'] <= 49:
            grade_values.append(0)
    counter = 0
    total_points_list = []
    # Get point total
    for details in book.values():
        total_points_value = details['credit'] * grade_values[counter]
        total_points_list.append(total_points_value)
        counter += 1

    attempted = []
    # Get attempted credits
    for details in book.values():
        attempted.append(details['credit'])
    return sum(total_points_list) / sum(attempted)


if __name__ == '__main__':
    grade_book = {}
    print('~~Enter your course information to get your GPA~~')
    while True:
        try:
            while True:
                user_course_number = input('Enter course number(Enter nothing to calculate GPA): ')
                if user_course_number == '':
                    break
                user_credit_value = int(input('Enter credit value: '))
                user_score = int(input('Enter your grade (Multiple of 5): '))
                if user_score < 0 or user_score > 100:
                    print('Your grade must be between 0 and 100')
                if user_score % 5 != 0:
                    print('Your grade must be divisible by 5!')
                    continue
                grade_book[user_course_number] = {'credit': user_credit_value, 'score': user_score}
            print(f'Your GPA is: {calculate_gpa(grade_book)}')
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        except ZeroDivisionError as zde:
            print('You must add at least one course')
        except Exception as e:
            print(type(e), e)
        else:
            break
