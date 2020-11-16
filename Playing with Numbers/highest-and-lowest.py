def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split()]
    numbers = [max(numbers), min(numbers)]
    numbers = ' '.join([str(elem) for elem in numbers])
    print(numbers)
    return numbers