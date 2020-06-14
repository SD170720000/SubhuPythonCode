# (2.) You are given the year, and you have to write a function to check if the year is a leap or not. 


def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))

