from AndXOrTree import AndXOrTree
from AndXorNode import AndXorNode
from copy import deepcopy
from random import randint

class Env:
    def __init__(self):
        self.rootNode = AndXorNode(None, False, None, None, 1, 12, 0)
        self.optional1 = AndXorNode(None, False, None, None, 200, 5, 1)
        self.optional2 = AndXorNode(None, False, None, None, 3, 6, 2)
        self.and2 = AndXorNode(None, True, None, None, 5, 8, 3)
        self.optional5 = AndXorNode(None, False, None, None, 6, 11, 4)
        self.optional6 = AndXorNode(None, False, None, None, 7, 9, 5)

        self.and1 = AndXorNode(None, True, None, None, 11, 2, 6)

        self.leaf1 = AndXorNode(None, False, None, None, 200, 142, 7)
        self.leaf2 = AndXorNode(None, False, None, None, 22, 152, 8)
        self.leaf3 = AndXorNode(None, False, None, None, 23, 172, 9)
        self.leaf4 = AndXorNode(None, False, None, None, 2000, 192, 10)
        self.leaf5 = AndXorNode(None, False, None, None, 25, 142, 11)

        self.rootNode.setLeft(self.optional1)
        self.rootNode.setRight(self.optional2)

        self.optional1.left = self.leaf1
        self.optional1.right = self.and2
        self.optional1.parent = self.rootNode
        self.and2.left = self.optional5
        self.and2.right = self.optional6
        self.and2.parent = self.optional1
        self.optional6.left = self.leaf4
        self.optional6.parent = self.and2
        self.optional5.parent = self.and2
        self.leaf4.parent = self.optional6

        self.leaf1.parent = self.optional1

        self.optional2.left = self.and1
        self.optional2.right = self.leaf5
        self.optional2.parent = self.rootNode

        self.and1.left = self.leaf2
        self.and1.right = self.leaf3
        self.and1.parent = self.optional2

        self.leaf5.parent = self.optional2
        self.leaf2.parent = self.and1
        self.leaf3.parent = self.and1

        self.tree1 = AndXOrTree(self.rootNode)
        self.treeBeforeNormalizing = deepcopy(self.tree1)
        self.tree1.normalize(self.tree1.getRootNode())
        self.normalizedtree = self.tree1
        self.position = self.rootNode

    def stepInDirection(self, goLeft=True):
        return self.step(goLeft)

    def stepInRandomDirection(self):
        randomNumber = randint(0, 100)
        if(randomNumber > 50):
            return self.step(True)
        else:
            return self.step(False)

    def step(self, goLeft):
        done = False
        reward = 0
        next_state = None
        info = None

        if goLeft and self.position.left != None:
            next_state = self.position.left
            info = 0

        elif goLeft and self.position.right != None:
            next_state = self.position.right
            info = 1

        if not goLeft and self.position.right != None:
            next_state = self.position.right
            info = 1
        elif not goLeft and self.position.left != None:
            next_state = self.position.left
            info = 0

        if next_state.isLeafNode():
           done = True

        reward = next_state.value - next_state.cost
        self.position = next_state

        return (next_state, reward, done, info)

    def reset(self):
        self.position = self.rootNode
        return self.position

if __name__ == '__main__':
    env = Env()

    rn = env.tree1.getRootNode()
    print('Tree, before normalizing')
    print(env.treeBeforeNormalizing.getRootNode())
    print('###########################')
    print('Tree, after normalizing')
    print(env.normalizedtree.getRootNode())
