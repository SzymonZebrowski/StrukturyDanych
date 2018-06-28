class ListNode():
    def __init__(self, val):
        self.value=val
        self.prev=None
        self.next=None

class List():
    def __init__(self):
        self.size=0
        self.first=None
        self.last=None

    def push_back(self, val):
        new = ListNode(val)
        self.size+=1
        if(self.first==None):
            self.first=self.last=new
        else:
            new.prev=self.last
            new.next=None
            new.prev.next=new
            self.last=new

    def push_front(self, val):
        new = ListNode(val)
        self.size += 1
        if (self.first == None):
            self.first = self.last = new
        else:
            new.next = self.first
            new.prev = None
            new.next.prev = new
            self.first = new

    def pop_front(self):
        if(self.size==0): return
        self.size-=1
        self.first=self.first.next
        self.first.prev=None

    def pop_back(self):
        if(self.size==0): return
        self.size-=1
        self.last=self.last.prev
        self.last.next=None

    def search(self, val):
        tmp=self.first
        while(tmp.value!=val):
            tmp=tmp.next
        return tmp

    def find_index(self, i):
        if(i<0 or i>self.size): return
        tmp=self.first
        index=0
        while(index<i):
            index+=1
            tmp=tmp.next

        return tmp

    def change_value(self, node, val):
        node.value=val

    def print(self):
        tmp=self.first
        while(tmp!=None):
            print(tmp.value, end=" ")
            tmp=tmp.next



