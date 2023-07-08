import argparse
from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit
from dfs import dfs
from bfs import bfs
from a_star import a_star
from policy_iteration import policy_iteration
from value_iteration import value_iteration

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--MazeSize', nargs='?', default="10x10", type=str)
    parser.add_argument('--Method', nargs='?', default="mdp_policy", type=str)
    args = parser.parse_args()
    MazeSize = args.MazeSize
    Method = args.Method
    print(f"The method using to solve the maze is {Method}")
    print(f"The maze size is {MazeSize}")

    m = maze()
    if MazeSize == "10x10":
        # m.CreateMaze(saveMaze=True)
        m.CreateMaze(loadMaze='maze//maze_10x10.csv')
    elif MazeSize == "30x30":
        m.CreateMaze(loadMaze='maze//maze_30x30.csv')
    elif MazeSize == "50x50":
        m.CreateMaze(loadMaze='maze//maze_50x50.csv')
    # print(m.maze_map)

    agent = agent(m, filled=True, footprints=True, color=COLOR.red)
    t = 0.0
    iteration = 0
    if Method == "bfs":
        #######
        # BFS #
        #######
        forward_path, iteration = bfs(m)
        m.tracePath({agent: forward_path}, delay=100)
        t = timeit(stmt='bfs(m)', number=10, globals=globals())
        textLabel(m, 'BFS', t)
    elif Method == "dfs":
        #######
        # DFS #
        #######
        forward_path, iteration = dfs(m)
        m.tracePath({agent: forward_path}, delay=100)
        t = timeit(stmt='dfs(m)', number=10, globals=globals())
        textLabel(m, 'DFS', t)
    elif Method == "astar":
        ##########
        # A Star #
        ##########
        search_path, a_path, forward_path, iteration = a_star(m)
        # a = agent(m, filled=True, footprints=True)
        # b = agent(m, 1,1,color=COLOR.yellow, footprints=True, filled=True)
        # m.tracePath({a: search_path}, delay=300)
        # m.tracePath({b: a_path})
        m.tracePath({agent: forward_path}, delay=100)
        t = timeit(stmt='a_star(m)', number=10, globals=globals())
        textLabel(m, 'A Star', t)
    elif Method == "mdp_value":
        ###################
        # Value Iteration #
        ###################
        V, optimal_value_path, iteration = value_iteration(m)
        # print('V:', V)
        # print('optimal_policy:', optimal_policy_path)
        m.tracePath({agent: optimal_value_path}, delay=100)
        t = timeit(stmt='value_iteration(m)', number=1, globals=globals())
        textLabel(m, 'Value Iteration', t)
    elif Method == "mdp_policy":
        ####################
        # Policy Iteration #
        ####################
        optimal_policy_path, iteration = policy_iteration(m)
        # print(optimal_policy_path)
        m.tracePath({agent: optimal_policy_path}, delay=100)
        t = timeit(stmt='policy_iteration(m)', number=1, globals=globals())
        textLabel(m, 'Policy Iteration', t)

    print(f"The time taken is {t}")
    print(f"Iteration: {iteration}")
    m.run()
