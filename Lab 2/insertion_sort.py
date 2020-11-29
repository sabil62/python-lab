def insertionSort (data):
    length = len(data)

    for i in range(1, length):
        key = data[i]
        j = i - 1

        while ( (j+1) > 0 and data[j] > key):
            data[j+1] = data[j]
            j = j - 1

        data[j+1] = key
