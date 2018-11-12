from binarytree import Node

class AndXorNode:
    def __init__(self, parent, andGate=False, left=None, right=None, id=None, cost=0):
        Node.__init__(self, id)
        self.parent = parent
        self.andGate = andGate
        self.left = left
        self.right = right
        self.cost = cost

    def isLeafNode(self):
        return self.left == None and self.right == None

    def isAndGate(self):
        return self.andGate and self.left != None and self.right != None

    def getCost(self):
        return self.cost

    def getId(self):
        return self.id

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def attachChildNode(self, node):
        if node == None:
            return False
        if self.left == None:
            self.left = node
        else:
            self.right = node

    def setParent(self, node):
        self.parent = node

    def setLeft(self, leftNode):
        self.left = leftNode

    def setRight(self, rightNode):
        self.right = rightNode

    def __str__(self):
        return Node.__str__(self)
