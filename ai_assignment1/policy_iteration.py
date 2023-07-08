import numpy as np


def policy_iteration(m, gamma=1, epsilon=0.1):
    # policy iteration
    iteration = 0
    pi = {cell: 'E' for cell in m.grid}
    while True:
        iteration += 1
        V = policy_evaluation(pi, m, gamma, epsilon)
        new_pi = policy_improvement(m, V)
        if pi == new_pi:
            break
        pi = new_pi
    # print('V:', V)
    # print('optimal_policy:', pi)

    # visualize the optimal path
    optimal_policy_path = {}
    cell = (m.rows, m.cols)
    while cell != (1, 1):
        # print(cell)
        action = pi[cell]
        if action == 'E':
            next_cell = (cell[0], cell[1] + 1)
        elif action == 'S':
            next_cell = (cell[0] + 1, cell[1])
        elif action == 'N':
            next_cell = (cell[0] - 1, cell[1])
        elif action == 'W':
            next_cell = (cell[0], cell[1] - 1)
        optimal_policy_path[cell] = next_cell
        cell = next_cell
    # print(optimal_policy_path)
    return optimal_policy_path, iteration


def policy_evaluation(pi, m, gamma=1, epsilon=0.1):
    states = m.grid
    states.reverse()

    V = {cell: 0 for cell in m.grid}

    while True:
        delta = 0
        oldV = dict(V)
        for state in states:
            if state == (1, 1):
                continue
            else:
                action = pi[state]
                next_state, r = reward_function(state, action, m)
                if r == -1000:
                    V[state] = r
                else:
                    V[state] = r + gamma * oldV[next_state]
                delta = max(np.abs(oldV[state] - V[state]), delta)

        if delta < epsilon:
            break

    return V


def policy_improvement(m, V, gamma=1):
    states = m.grid
    states.reverse()
    actions = ['E', 'W', 'N', 'S']

    pi = {cell: None for cell in m.grid}

    for state in states:
        if state == (1, 1):
            continue
        else:
            Q = {action: 0 for action in actions}
            for action in actions:
                next_state, r = reward_function(state, action, m)
                if r == -1000:
                    Q[action] = r
                else:
                    Q[action] = r + gamma * V[next_state]
            pi[state] = max(Q, key=Q.get)

    return pi


def reward_function(state, action, m):
    # can't move > no value, can move +1
    if m.maze_map[state][action]:
        if action == 'E':
            next_state = (state[0], state[1] + 1)
        elif action == 'S':
            next_state = (state[0] + 1, state[1])
        elif action == 'N':
            next_state = (state[0] - 1, state[1])
        elif action == 'W':
            next_state = (state[0], state[1] - 1)
        if next_state == (1, 1):
            return next_state, 0
        else:
            return next_state, -1
    else:
        return None, -1000