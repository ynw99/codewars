def even_or_odd(s):
    even, odd = [], []
    [odd.append(int(i)) if int(i)%2 == True else even.append(int(i)) for i in str(s)]
    return 'Odd is greater than Even' if sum(odd) > sum(even) \
            else'Even is greater than Odd' if sum(even) > sum(odd) \
            else 'Even and Odd are the same'