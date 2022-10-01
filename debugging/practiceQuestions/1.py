# Q1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

spam = int(input("Enter any random number: "))

assert spam > 10, "spam is less than 10"