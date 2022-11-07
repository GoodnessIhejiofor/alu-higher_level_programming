#!/usr/bin/python3
safe_function=__import__('101-safe_function').safe_function


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result

result = safe_function(magic_calculation, 10, 2)
print("result of magic_calculation: {}".format(result))
