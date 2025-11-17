def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def weird_or_not(n):
    if n % 2 == 1:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


def even_numbers_if(a, b):
    if a > b:
        a, b = b, a
    if a % 2 != 0:
        a += 1
    if a > b:
        return []
    return [a] + even_numbers_if(a + 2, b)


def even_numbers_no_if(a, b):
    a, b = min(a, b), max(a, b)
    a = a + (a % 2)
    if a > b:
        return []
    return [a] + even_numbers_no_if(a + 2, b)


# Example outputs
print(is_leap(2024))
print(weird_or_not(3))
print(even_numbers_if(3, 15))
print(even_numbers_no_if(3, 15))
