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


def quick_sort(data):
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


def counting_sort(data, minimum, maximum):
    histogram = [0 for _ in range(minimum, maximum+1)]
    out = [0 for _ in range(len(data))]

    for i in range(len(data)):
        histogram[data[i]] += 1

    for i in range(minimum+1, maximum+1):
        histogram[i] += histogram[i-1]

    for i in range(len(data)-1, -1, -1):
        out[histogram[data[i]]-1] = data[i]
        histogram[data[i]] -= 1

    data = out
    return data


def radix_sort(data):
    maximum = max(data)

    def counting_sort(data, exp):
        n = len(data)
        histogram = [0 for _ in range(10)]
        out = [0 for _ in range(n)]

        for i in range(n):
            histogram[data[i]//exp % 10] += 1


        for i in range(1, 10):
            histogram[i] += histogram[i-1]
        #now histogram[x] contains position in list at which the l
        # ast occurence of 'x' will appear.
        #for example
        #   range : 0-5
        #   data = [1,2,1,3,1,5,2,0,2,5]
        #   prev_histogram = [1,3,3,1,0,2]
        #   histogram = [1,4,7,8,8,10]
        #histogram shows position
        #
        #

        i = n - 1
        while i >= 0:
            out[histogram[data[i]//exp % 10] - 1] = data[i]
            histogram[data[i]//exp % 10] -= 1
            i -= 1

        data = out
        return data

    e = 1
    while (maximum // e) > 0:
        data = counting_sort(data, e)
        e *= 10

    return data


def heap_sort(data):
    n = len(data)

    def left(i): return 2*i + 1
    def right(i): return 2*(i+1)

    def heapify(i, n):
        print(data)
        largest = i
        l = left(i)
        r = right(i)

        if l < n and data[largest] < data[l]:
            largest = l

        if r < n and data[largest] < data[r]:
            largest = r

        if largest != i:
            data[i], data[largest] = data[largest], data[i]

            heapify(largest, n)

    def build_heap():
        for i in range(n//2, -1, -1):
            heapify(i, n)

    build_heap()
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(0, i)

    return data