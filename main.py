from Basic.List import List
from Trees.BST import BST
from Trees.BST import BSTNode
from Trees.RBT import RBTNode
from Trees.RBT import RBT


tree = BST()
tree.add(5)
tree.add(1)
tree.add(12)
tree.add(7)
tree.add(8)

tree.inorder_print(tree.root)
print()
tree.postorder_print(tree.root)
print()
tree.preorder_print(tree.root)
print()

rbt = RBT()
rbt.add(11)

rbt.inorder_print(rbt.root)
print()
rbt.preorder_print(rbt.root)
print()




