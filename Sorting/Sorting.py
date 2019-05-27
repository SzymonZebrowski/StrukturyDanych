# all algo
# rithms sort in ascending order


def bubble_sort(data):
    n = len(data)
    for i in range(0, n):
        swapped = False
        for j in range(0, n-1):
            if(data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def quicksort(data):
    def quicksort_util(data, l, r):
        i, j = l, r
        p = data[(i+j)//2]
        while i<=j:
            while data[i]<p: i+=1
            while data[j]>p: j-=1
            if i<=j:
                data[i], data[j] = data[j], data[i]
                i+=1
                j-=1

        if l<j: quicksort_util(data, l, j)
        if i<r: quicksort_util(data, i, r)
        return data

    return quicksort_util(data, 0, len(data)-1)


def counting_sort(data, maximum):
    minimum = 0
    n_elems = maximum - minimum
    histogram = [0 for _ in range(minimum, maximum+1)]

    for i in range(len(data)):
        histogram[data[i]] += 1

    index = 0
    for i in range(n_elems):
        while histogram[i] > 0:
            data[index] = i
            histogram[i] -= 1
            index += 1

    return data
