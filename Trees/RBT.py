import Trees.BST
BLACK = "B"
RED = "R"


class RBTNode(Trees.BST.BSTNode):
    def __init__(self, val):
        self.color = BLACK
        super().__init__(val)


class RBT(Trees.BST.BST):
    def __init__(self):
        super().__init__()

    def get_color(self, x):
        if x != None:
            return x.color
        else:
            return BLACK

    def add(self, val):
        x = super().add(val, RBTNode)
        x.color = RED

        if x == self.root:
            x.color=BLACK

        while x != self.root and x.parent.color == RED:
            if x.parent == x.parent.parent.left:
                uncle = x.parent.parent.right
                if self.get_color(uncle) == RED:
                    x.parent.color = BLACK
                    uncle.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.left_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.right_rotate(x.parent.parent)
            else:
                uncle = x.parent.parent.left
                if self.get_color(uncle) == RED:
                    x.parent.color = BLACK
                    uncle.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.right_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.left_rotate(x.parent.parent)
            self.root.color = BLACK


    def left_rotate(self, x):
        y = x.right
        if y == None:
            return
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        if y == None:
            return
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def delete(self, val):
        y = super().delete(val)
        print(y.value,y.color)


    def inorder_print(self, node):
        if(node!=None):
            self.inorder_print(node.left)
            s = str(node.value) + node.color
            print(s, end=" ")
            self.inorder_print(node.right)

    def preorder_print(self, node):
        if(node!=None):
            s = str(node.value) + node.color
            print(s, end=" ")
            self.preorder_print(node.left)
            self.preorder_print(node.right)

    def postorder_print(self, node):
        if (node != None):
            self.postorder_print(node.left)
            self.postorder_print(node.right)
            s = str(node.value)+node.color
            print(s, end=" ")