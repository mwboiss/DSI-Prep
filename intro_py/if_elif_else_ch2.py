def is_divisible_by(num,divisor1,divisor2):

    if num % divisor1 == 0 and num % divisor2 == 0:
            return f"This number is divisble by {divisor1} and {divisor2}."
    elif num % divisor1 == 0:
        return f"This number is divisble by {divisor1}."

    elif num % divisor2 == 0:
        return f"This number is divisble by {divisor2}."

    else:
        return f"This number is not divisble by either {divisor1} or {divisor2}."

print(is_divisible_by(12,3,4))