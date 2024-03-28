def sliding_window_max(num_list, size):
    result = []
    window = []
    for i, num in enumerate(num_list):

        while window and window[0][1] < i - size + 1:
            window.pop(0)
        while window and window[-1][0] < num:
            window.pop()
        window.append((num, i))
        if i >= size - 1:
            result.append(window[0][0])
    return result


num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
size = 3
print(sliding_window_max(num_list, size))  