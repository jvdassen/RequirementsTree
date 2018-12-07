import random
import numpy
from AndXorNode import AndXorNode
from Environment import Env

def printOptimalSubTree(q_table, tree):
    root = tree.getRootNode()

    rewards = [ root.value - root.cost ]
    result = AndXorNode(root.parent, root.andGate, None, None, root.value, root.cost, root.getId())
    resultLeaf = result
    temp = None

    def addNextStep(startNode, resultLeaf):
        best_action = numpy.argmax(q_table[startNode.getId()])
        if best_action == 0:
            temp = startNode.left
        else:
            temp = startNode.right

        if not tree.requirementExistsInSomeParent(resultLeaf, temp.getId()):
            resultLeaf.left = AndXorNode(temp.parent, temp.andGate, None, None, temp.value, temp.cost, temp.getId())
            rewards.append(temp.value - temp.cost)
            resultLeaf = resultLeaf.left

        if not temp.isLeafNode():
            addNextStep(temp, resultLeaf)


    addNextStep(root, resultLeaf)

    totalReward = numpy.sum(rewards)

    print('The optimal way to traverse the tree with a total reward of ' + str(totalReward) + ' would be:')
    print(result)

if __name__ == '__main__':
    environment = Env()

    alpha = 0.1
    gamma = 0.6
    epsilon = 0.3

    number_of_episodes = 10000

    q_table = numpy.zeros([environment.normalizedtree.getNumberOfNodes(), 2])

    for i in range(1, number_of_episodes):
        state = environment.reset()
        visited_states = []

        penalties, reward = 0, 0
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                next_state, reward, done, info = environment.stepInRandomDirection()
            else:
                best_action = numpy.argmax(q_table[state.nodeid])
                goLeft = best_action == 0

                next_state, reward, done, info = environment.stepInDirection(goLeft)

            action_taken = info

            if next_state.getId() not in visited_states:

                old_val = q_table[state.nodeid, action_taken]
                next_max = numpy.max(q_table[next_state.nodeid])

                new_val = (1 - alpha) * old_val + alpha * (reward + gamma * next_max)
                q_table[state.nodeid, action_taken] = new_val
                visited_states.append(next_state.getId())

            state = next_state


        if i % 1000 == 0:
            print('Q table after' + str(i) + ' episodes')
            print(q_table)
            nodes = environment.normalizedtree.getAllLowerNodes(environment.normalizedtree.getRootNode())
            print('Lookup table for nodes in the q_table. Each row of the q_table corresponds to the nodeid of a node. In the visual graph, only the values of the nodes are displayed.')
            for index, node in enumerate(nodes):
                print(str(index) + ': ' + node.__repr__() + '\n')
            print(environment.normalizedtree.getRootNode())

    print('Learning from ' + str(i) + ' episodes completed. Result:')
    printOptimalSubTree(q_table, environment.normalizedtree)

