def get_fraction(value, hij):
    arr = [4, 5, 2, 0]  # a list of numbers
    hij = arr[hij]  # if idx is > arr length, IndexError will be raised
    value / hij  # if idx_value == 0, ZeroDivisionError will be raised


if __name__ == '__main__':
    # set 'value' and 'idx'
    value = 54
    hij = 5
    # call function in a try-except statement.
    try:
        result = get_fraction(value, hij)
        print("Fraction is ", result)
    except (IndexError, ZeroDivisionError) as ex:
        print(ex)