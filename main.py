from Basic.List import List
from Basic.Stack import Stack
from Trees.BST import BST
from Trees.BST import Node
from Heaps.Heap import Heap

H=[64,2,32,4,16,8, 5 ,21 ,512, -1, 15, 129, 123, 54, 23, 32]

heap=Heap(H)
heap.print()
print("\n")
heap.build_heap()
heap.print()
print("\n")
heap.heapsort()
heap.print()
print("\n")
heap.pop()
heap.pop()
heap.pop()
heap.pop()
heap.push(666)
heap.build_heap()
heap.print()


