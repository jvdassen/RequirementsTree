from Environment import Env
import numpy
import random
from AndXorNode import AndXorNode


def update_critic(utility_matrix, state, next_state, reward, alpha, gamma):
    utility = utility_matrix[state]
    utility_next = utility_matrix[next_state]
    delta = reward + gamma * utility_next - utility
    utility_matrix[state] += alpha * (delta)

    return utility_matrix, delta

def update_actor(state_action_matrix, state, action, delta):
    beta = 1
    state_action_matrix[state, action] += beta * delta

    return state_action_matrix

if __name__ == '__main__':
    environment = Env()

    alpha = 0.1
    gamma = 0.99
    epsilon = 0.01

    number_of_episodes = 10000

    #state_action_pairs = numpy.zeros([environment.normalizedtree.getNumberOfNodes(), 2])
    state_action_pairs = numpy.full((environment.normalizedtree.getNumberOfNodes(), 2), 0.5)
    utility_matrix = numpy.zeros([environment.normalizedtree.getNumberOfNodes()])

    softmax = lambda vals: numpy.exp(vals- numpy.max(vals)) / numpy.sum(numpy.exp(vals - numpy.max(vals)))

    for i in range(1, number_of_episodes):
        state = environment.reset(randomStart=True)
        visited_states = []

        penalties, reward = 0, 0
        done = False

        while not done:
            action_array = state_action_pairs[state.nodeid]
            action_distribution = softmax(action_array)

            action = numpy.random.choice(2, 1, p=action_distribution)[0]

            if i % 1000 == 0:
                print()

            goLeft = action == 0
            next_state, reward, done, info = environment.stepInDirection(goLeft)
            action_taken = info

            if next_state.nodeid not in visited_states:
                utility_matrix, delta = update_critic(utility_matrix, state.nodeid, next_state.nodeid, reward, gamma, alpha)
                state_action_pairs = update_actor(state_action_pairs, state.nodeid, action_taken, delta)

            if done:
                # Manually update the utilites corresponding to a leaf node with value - cost
                utility_matrix[next_state.nodeid] = reward

            visited_states.append(next_state.nodeid)
            state = next_state


        if i % 1000 == 0:
            print('Utility values after' + str(i) + ' episodes')
            print(utility_matrix)
            nodes = environment.normalizedtree.getAllLowerNodes(environment.normalizedtree.getRootNode())
            print('Lookup table for nodes in the utility_table. Each index of the table corresponds to the nodeid of a node. In the visual graph, only the values of the nodes are displayed.')
            for index, node in enumerate(nodes):
                print(str(index) + ': ' + node.__repr__() + '\n')
            print(environment.normalizedtree.getRootNode())

    print('Learning from ' + str(i) + ' episodes completed. Result:')
    print(utility_matrix)
    print(state_action_pairs)

    #printOptimalSubTree(state_action_pairs, environment.normalizedtree)

