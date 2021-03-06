from binarytree import Node

class AndXorNode:
    def __init__(self, parent, andGate=False, left=None, right=None, value=None, cost=0, id=0):
        Node.__init__(self, value)
        self.parent = parent
        self.andGate = andGate
        self.left = left
        self.right = right
        self.cost = cost
        self.requirementid = id
        self.nodeid = 0

    def isLeafNode(self):
        return self.left == None and self.right == None

    def isAndGate(self):
        return self.andGate and self.left != None and self.right != None

    def getCost(self):
        return self.cost

    def getId(self):
        return self.requirementid

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

    def setNodeId(self, nodeid):
        self.nodeid = nodeid

    def __str__(self):
        return Node.__str__(self)

    def __repr__(self):
        return 'Node {id:'+ str(self.getId()) + ', value:' + str(self.value) + ', cost:' + str(self.cost) + ', nodeid:' + str(self.nodeid) +  '}'
