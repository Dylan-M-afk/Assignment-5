def calculate_gpa(book: dict):
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
    # The CNA GPA calc is missing a lot of values? like 75-80
    for details in book.values():
        if details['score'] >= 80:
            grade_values.append(4)
        elif 70 <= details['score'] <= 75:
            grade_values.append(3)
        elif 60 <= details['score'] <= 65:
            grade_values.append(2)
        elif 50 <= details['score'] <= 55:
            grade_values.append(1)
        elif details['score'] <= 49:
            grade_values.append(0)
    counter = 0
    total_points_list = []
    for details in book.values():
        total_points_value = details['credit'] * grade_values[counter]
        total_points_list.append(total_points_value)
        counter += 1
    attempted = []
    for details in book.values():
        attempted.append(details['credit'])
    return sum(total_points_list) / sum(attempted)


if __name__ == '__main__':
    while True:
        try:
            while True:
                user_course_number = input('Enter course number: ')
                if user_course_number == '':
                    break
                user_credit_value = int(input('Enter credit value: '))
                user_score = int(input('Enter your grade (Multiple of 5): '))
                if user_score < 0 or user_score > 100:
                    print('Your grade must be between 0 and 100')
                if user_score % 5 != 0:
                    print('Your grade must be divisible by 5!')
                    continue
                grade_book = {user_course_number: {'credit': user_credit_value, 'score': user_score}}
            # If undefined a name error will be caught
            print(f'Your GPA is: {calculate_gpa(grade_book)}')
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        except NameError as ne:
            print('You must add at least one course')
        except Exception as e:
            print(type(e), e)
        else:
            break
