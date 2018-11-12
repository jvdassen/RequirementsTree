from AndOrTree import AndOrTree
from AndXorNode import AndXorNode

rootNode = AndXorNode(None, False, None, None, 1, 12)
optional1 = AndXorNode(None, False, None, None, 2, 5)
optional2 = AndXorNode(None, False, None, None, 3, 6)
optional3 = AndXorNode(None, False, None, None, 4, 7)

and1 = AndXorNode(None, True, None, None, 5, 2)

leaf1 = AndXorNode(None, False, None, None, 21, 142)
leaf2 = AndXorNode(None, False, None, None, 22, 152)
leaf3 = AndXorNode(None, False, None, None, 23, 172)
leaf4 = AndXorNode(None, False, None, None, 24, 192)
leaf5 = AndXorNode(None, False, None, None, 25, 142)

rootNode.setLeft(optional1)
rootNode.setRight(optional2)

optional1.left = leaf1
optional1.right = leaf4

optional2.left = and1
optional2.right = leaf5

and1.left = leaf2
and1.right = leaf3

tree1 = AndOrTree(rootNode)




rn = tree1.getRootNode()
print('Tree, before normalizing')
print('Number of leaf nodes:')
print(len(tree1.getDeepLeafNodes(tree1.getRootNode())))

print(tree1.getRootNode())
print('###########################')
print('Tree, after normalizing')
tree1.normalize(tree1.getRootNode())
print(tree1.getRootNode())
print('Number of leaf nodes:')
print(len(tree1.getDeepLeafNodes(tree1.getRootNode())))