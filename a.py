def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    stepCount = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        stepCount += 1
    return stepCount
