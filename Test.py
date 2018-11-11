from AndOrTree import AndOrTree
from AndXorNode import AndXorNode

rootNode = AndXorNode(None, False, None, None, 1, 12)
optional1 = AndXorNode(None, False, None, None, 2, 5)
optional2 = AndXorNode(None, False, None, None, 3, 6)
optional3 = AndXorNode(None, False, None, None, 4, 7)

and1 = AndXorNode(None, True, None, None, 5, 2)

leaf1 = AndXorNode(None, False, None, None, 6, 142)
leaf2 = AndXorNode(None, False, None, None, 7, 152)
leaf3 = AndXorNode(None, False, None, None, 8, 172)
leaf4 = AndXorNode(None, False, None, None, 9, 192)
leaf5 = AndXorNode(None, False, None, None, 10, 142)

rootNode.setLeft(optional1)
rootNode.setRight(optional2)

optional1.left = leaf1
optional1.right = leaf4

optional2.left = and1
optional2.right = leaf5

and1.left = leaf2
and1.right = leaf3

tree1 = AndOrTree(rootNode)

print(len(tree1.getDeepLeafNodes(tree1.getRootNode())))
print(tree1.getRootNode())
# print(tree1.normalize(tree1.getRootNode()))
