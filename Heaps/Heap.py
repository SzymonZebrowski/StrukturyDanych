class Heap():
    def __init__(self, array):
        self.array=array
        self.currentSize=len(array)

    def push(self, val):
        self.array.append(val)
        self.currentSize+=1

    def pop(self):
        self.array.pop(self.currentSize-1)
        self.currentSize-=1

    def left(self, i):
        return i*2

    def right(self,i):
        return i*2+1

    def parent(self, i):
        return i//2

    def build_heap(self):
        for x in range(self.currentSize//2, -1, -1):
            self.heapify(x)

    def heapify(self, i):
        while(i<self.currentSize):
            index=i
            if(self.left(i)<self.currentSize and self.array[self.left(i)]>self.array[index]):
                index=self.left(i)
            if(self.right(i)<self.currentSize and self.array[self.right(i)]>self.array[index]):
                index=self.right(i)
            if(index==i):
                return

            tmp=self.array[i]
            self.array[i]=self.array[index]
            self.array[index]=tmp

            i=index

    def print(self):
        for x in self.array:
            print(x, end=" ")

    def heapsort(self):
        tmp=self.currentSize
        while(self.currentSize>0):
            t=self.array[0]
            self.array[0]=self.array[self.currentSize-1]
            self.array[self.currentSize-1]=t
            self.currentSize -= 1
            self.heapify(0)


        self.currentSize=tmp
