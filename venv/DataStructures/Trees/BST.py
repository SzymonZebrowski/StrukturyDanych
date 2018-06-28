class Node():
    def __init__(self, val):
        self.value=val
        self.parent=None
        self.left=None
        self.right=None

class BST():
    def __init__(self):
        self.root=None

    def add(self, val):
        new=Node(val)
        if(self.root==None):
            self.root=new
            return

        tmp=self.root
        while(True):
            if(val>tmp.value):
                if(tmp.right!=None):
                    tmp=tmp.right
                else:
                    tmp.right=new
                    new.parent=tmp
                    break
            else:
                if (tmp.left != None):
                    tmp = tmp.left
                else:
                    tmp.left = new
                    new.parent = tmp
                    break

    def find(self, val):
        tmp=self.root
        while(True):
            if(tmp==None):
                break
            if(val>tmp.value):
                tmp=tmp.right
            elif(val<tmp.value):
                tmp=tmp.left
            else:
                break
        if(tmp!=None):
            return tmp
        else:
            print("Nie znaleziono klucza")



    def inorder_print(self, node):
        if(node!=None):
            self.inorder_print(node.left)
            print(node.value, end=" ")
            self.inorder_print(node.right)

    def preorder_print(self, node):
        if(node!=None):
            print(node.value, end=" ")
            self.preorder_print(node.left)
            self.preorder_print(node.right)

    def postorder_print(self, node):
        if (node != None):
            self.postorder_print(node.left)
            self.postorder_print(node.right)
            print(node.value, end=" ")

