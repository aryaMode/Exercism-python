def is_armstrong_number(number):
    number = str(number)
    num_raise = len(number)
    final_num = 0
    for char in number:
        final_num += int(char)**num_raise

    if int(final_num) == int(number):
        return True
    else:
        return False

