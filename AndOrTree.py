from AndXorNode import Node
from copy import deepcopy

class AndOrTree:
    """"A class that represents a requirements tree, where each non-leaf node can be AND or OR"""
    def __init__(self, rootNode=None):
        self.rootNode = rootNode

    def setRootNode(self, node):
        self.rootNode = node

    def getRootNode(self):
        return self.rootNode

    def normalize(self, node):
        if node.isLeafNode():
            return True
        if node.isAndGate():
            """ get all leaf nodes from one side and mount deep copies of the node as new child """
            allDeepLeafs = self.getDeepLeafNodes(node)
            for leafNode in allDeepLeafs:
                deepCopyForLeafNode = deepcopy(node)
                deepCopyForLeafNode.setParent(leafNode)
                leafNode.attachChildNode(deepcopy(node))
        self.normalize(node.left)
        self.normalize(node.right)


    def getDeepLeafNodes(self, node):
        leafnodes = []
        if node.isLeafNode():
            return [ node ]
        left = node.left
        right = node.right

        if left != None:
            childsLeafs = self.getDeepLeafNodes(left)
            leafnodes += childsLeafs

        if right != None:
            childsLeafs = self.getDeepLeafNodes(right)
            leafnodes += childsLeafs

        return leafnodes

