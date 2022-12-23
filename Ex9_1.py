def even_odd_sum(num_list):
    result = [0, 0]
    for idx in range(len(num_list)):
        if idx % 2 == 0:
            result[0] += num_list[idx]
        else:
            result[1] += num_list[idx]
    return result

print(even_odd_sum([10, 20, 30, 40, 50, 60]))
