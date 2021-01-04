import math


def compute_square_root(number):
    # compute the square root using the math library
    result = math.sqr(number)
    return result


if __name__ == '__main__':
    # get input to compute from user
    number = int(input("Compute Square root of: "))
    # call function to compute square root