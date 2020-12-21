def bubble_sort(data: list) -> list:
    to_index = len(data)
    print('test_data: ', data)

    while to_index > 1:
        to_index -= 1
        for i in range(to_index):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

    print('sorted: ', data)
    return data
