class Node():
    def __init__(self, val):
        self.next=None
        self.value=val

class Stack():
    def __init__(self, s):
        self.size=0
        self.top=None
        self.max_size=s

    def push(self, val):
        if (self.size == self.max_size):
            print("Stack overflow")
            return

        node=Node(val)
        if(self.top==None):
            self.top=node
            self.size+=1
        else:
            node.next=self.top
            self.top=node
            self.size+=1

    def print(self):
        tmp=self.top
        while(tmp!=None):
            print(tmp.value, end=" ")
            tmp=tmp.next

    def pop(self):
        if(self.size==0):
            print("Stack is empty")
            return
        tmp=self.top
        self.top=self.top.next
        self.size-=1
        return tmp.value



