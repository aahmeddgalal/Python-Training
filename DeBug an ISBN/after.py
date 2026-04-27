def validate_isbn(isbn, length):

    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]

    try:
        if length == 10:
            main_digits_list = [int(d) for d in main_digits]
            expected_check_digit = calculate_check_digit_10(main_digits_list)
        else:
            main_digits_list = [int(d) for d in main_digits]
            expected_check_digit = calculate_check_digit_13(main_digits_list)

    except ValueError:
        print('Invalid character was found.')
        return

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    return str(result)


def main():
    user_input = input('Enter ISBN and length: ')


    try:
        values = user_input.split(',')
        isbn = values[0]

        if len(values) < 2:
            print('Enter comma-separated values.')
            return

        length_str = values[1]

        try:
            length = int(length_str)
        except ValueError:
            print('Length must be a number.')
            return

        if length not in [10, 13]:
            print('Length should be 10 or 13.')
            return

        validate_isbn(isbn, length)

    except IndexError:
        print('Enter comma-separated values.')
        return


main()
