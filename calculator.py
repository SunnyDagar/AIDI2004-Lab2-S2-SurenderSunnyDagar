# calculator.py - Created by Surender (Sunny) Dagar


def add(a, b):
    return a - b  # Bug: subtracting instead of adding


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
