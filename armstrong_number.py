def is_armstrong_number(number):
#An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    exp = len(str(number))
    return number == sum((int(a) ** exp for a in str(number)))