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

    for i in range(len(data)):
        histogram[data[i]] += 1

    index = 0
    for i in range(minimum, maximum+1):
        while histogram[i] > 0:
            data[index] = i
            histogram[i] -= 1
            index += 1

    return data


def radix_sort(data):
    maximum = max(data)

    def counting_sort(data, exp):
        n = len(data)
        histogram = [0 for _ in range(10)]
        out = [0 for _ in range(n)]

        for i in range(n):
            histogram[data[i]//exp % 10] += 1

        # print(histogram)
        # for i in range(1, 10):
        #     histogram[i] += histogram[i-1]
        # print(histogram)
        # i = n - 1
        # while i >= 0:
        #     out[histogram[data[i]//exp % 10] - 1] = data[i]
        #     histogram[data[i]//exp % 10] -= 1
        #     i -= 1



        def find_first(data, n, r):
            for i in range(0, len(data)):
                if int('0'*len(repr(exp))+repr(data[i])[-r]) == n:
                    return data[i]

        index = 0
        for i in range(0, 10):
            while histogram[i] > 0:
                x = find_first(data, i, len(repr(exp)))
                print(f"i={i}, x={x}")
                if x!=None:
                    data.remove(x)
                    out[index] = x
                    index += 1
                    histogram[i] -= 1
                else:
                    break
        data = out
        return data

    e = 1
    while (maximum // e) > 0:
        data = counting_sort(data, e)
        e *= 10

    return data
