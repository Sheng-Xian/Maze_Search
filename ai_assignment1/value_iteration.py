import numpy as np


def value_iteration(m, gamma=1, epsilon=0.01):
    states = m.grid
    states.reverse()
    actions = ['E', 'W', 'N', 'S']

    V = {cell: -1 for cell in m.grid}
    optimal_policy = {m: None for m in m.grid}

    iteration = 0

    while True:
        iteration += 1
        delta = 0
        oldV = dict(V)
        for state in states:
            Q = {action: 0 for action in actions}
            if state == (1, 1):
                continue
            else:
                for action in actions:
                    next_state, r = reward_function(state, action, m)
                    if r == -1000:
                        Q[action] = r
                    else:
                        Q[action] = r + gamma * oldV[next_state]
                V[state] = max(Q.values())
                optimal_policy[state] = max(Q, key=Q.get)
                delta = max(np.abs(oldV[state]-V[state]), delta)

        if delta < epsilon:
            print(f"Iteration = {iteration}")
            print(f"Delta = {delta}")
            break

    optimal_policy_path = {}
    cell = (m.rows, m.cols)
    while cell != (1, 1):
        action = optimal_policy[cell]
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
    return V, optimal_policy_path, iteration


def P(next_cell, cell, action):
    for action in 'ESNW':
        if action == 'E':
            next_cell = (cell[0], cell[1] + 1)
        elif action == 'S':
            next_cell = (cell[0] + 1, cell[1])
        elif action == 'N':
            next_cell = (cell[0] - 1, cell[1])
        elif action == 'W':
            next_cell = (cell[0], cell[1] - 1)
    return 1, next_cell


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


