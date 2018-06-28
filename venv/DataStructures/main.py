from Basic.List import List
from Trees.BST import BST
from Trees.BST import Node

list=List()

for x in range(0,10):
    list.push_back(x)

list.pop_back()
list.pop_front()
list.search(5).value=123
list.change_value(list.search(2), 15)


list.print()

print("\n\n\n")
bst=BST()
bst.add(10)
bst.add(15)
bst.add(13)
bst.add(6)
bst.add(1)
bst.add(4)

bst.inorder_print(bst.root)
print("\n")
