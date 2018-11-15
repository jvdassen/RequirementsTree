from TestEnv import Env
import random
import numpy

if __name__ == '__main__':
    environment = Env()

    alpha = 0.1
    gamma = 0.6
    epsilon = 0.1

    number_of_episodes = 1000

    q_table = numpy.zeros([environment.normalizedtree.getNumberOfNodes(), 2])

    for i in range(1, number_of_episodes):
        state = environment.reset()
        visited_states = []

        epochs, penalties, reward = 0, 0, 0
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                next_state, reward, done, info  = environment.stepInRandomDirection()
            else:
                best_action = numpy.argmax(q_table[state.id])
                goLeft = best_action == 0

                next_state, reward, done, info = environment.stepInDirection(goLeft)

            action_taken = info

            if not next_state.id in visited_states:

                old_val = q_table[state.id, action_taken]
                next_max = numpy.max(q_table[next_state.id])

                new_val = (1 - alpha) * old_val + alpha * (reward + gamma * next_max)
                q_table[state.id, action_taken] = new_val

            state = next_state
            epochs += 1


        if i % 100 == 0:
            print('Q table after' + str(i) + ' episodes')
            print(q_table)
            print(environment.normalizedtree.getRootNode())

lrlrl
