def get_count(input_str):
    return sum([True if char in ('a', 'e', 'i', 'u', 'o') else False for char in input_str])