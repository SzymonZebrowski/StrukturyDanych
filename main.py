from Basic.List import List
from Trees.BST import BST
from Trees.BST import Node

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


