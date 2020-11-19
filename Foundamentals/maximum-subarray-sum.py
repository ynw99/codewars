def max_sequence(arr):
    global_max = 0
    local_max = 0

    for num in arr:
        local_max = local_max + num
        if global_max < local_max:
            global_max = local_max
        if local_max < 0:
            local_max = 0
        
    return global_max