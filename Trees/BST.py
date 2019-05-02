class BSTNode():
    def __init__(self, val):
        self.value=val
        self.parent=None
        self.left=None
        self.right=None


class BST():
    def __init__(self):
        self.root=None

    def add(self, val, node_func=BSTNode):
        new=node_func(val)
        if(self.root==None):
            self.root=new
            return new

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
        return new

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
        return tmp

    def successor(self, val):
        tmp=self.find(val)
        if(tmp.right!=None):
            tmp=tmp.right
            while(tmp.left!=None):
                tmp=tmp.left
            return tmp
        else:
            p=tmp.parent
            while(p!=None):
                if(tmp!=p.right):
                    break
                tmp=p
                p=p.parent
        return p

    def predecessor(self, val):
        tmp = self.find(val)
        if (tmp.left != None):
            tmp = tmp.left
            while (tmp.right != None):
                tmp = tmp.right
            return tmp
        else:
            p = tmp.parent
            while (p != None):
                if (tmp != p.left):
                    break
                tmp = p
                p = p.parent
        return p

    def delete(self, val):
        node=self.find(val)
        if(node==None):
            print("Nie ma takiego klucza")
            return None

        if(node.left==None and node.right==None):
            if(node.parent.left==node):
                node.parent.left=None
            else:
                node.parent.right=None
        elif(node.left!=None and node.right!=None):
            tmp=self.successor(node.value)
            self.delete(tmp.value)
            node.value=tmp.value
        elif(node.left==None or node.right==None):
            if(node.left==None):
                if(node.parent.left==node):
                    node.parent.left=node.right
                else:
                    node.parent.right=node.right
            if (node.right == None):
                if (node.parent.right == node):
                    node.parent.right = node.left
                else:
                    node.parent.left = node.left
        return node

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
