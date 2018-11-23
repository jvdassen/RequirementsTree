from AndXorNode import Node
from copy import deepcopy

class AndXOrTree:
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
            deepCopyForLeafNode = deepcopy(node)
            deepCopyForLeafNode.andGate = False
            node.andGate = False

            for leafNode in allDeepLeafs:
                deepCopyForLeafNode.setParent(leafNode)
                leafNode.left = deepCopyForLeafNode

        if node.left != None:
            self.normalize(node.left)
        if node.right != None:
            self.normalize(node.right)

        self.regenerateNodeIds(self.getRootNode())

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

    def getAllLowerNodes(self, node):
        nodes = []

        def getchildren( node):
            nodes.append(node)
            if node.left != None:
                getchildren(node.left)
            if node.right != None:
                getchildren(node.right)

        getchildren(self.getRootNode())
        return nodes

    def getNumberOfLeafNodes(self):
        return len(self.getDeepLeafNodes(self.getRootNode()))

    def getNumberOfNodes(self):
        return len(self.getAllLowerNodes(self.getRootNode()))

    def valueExistsInSomeParent(self, node, value):
        if node.parent == None:
            return False
        if node.value == value:
            return True
        else:
            return self.valueExistsInSomeParent(node.parent, value)

    def regenerateNodeIds(self, node):
        if node != None:
            node.regenerateNodeId()
            self.regenerateNodeIds(node.left)
            self.regenerateNodeIds(node.right)
        else:
            return
