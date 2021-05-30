"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def calc_pow(first_term, second_term: int):  # Switched to calc_pow to avoid confusion with math.pow.

    # TIP: Adding <arg_name> : <data_type> applies type check over argument (Ex. second_term: int )

    return first_term ** second_term


def spit_float() -> float:
    return float(1)
