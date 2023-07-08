def dfs(maze):
    start = (maze.rows, maze.cols)
    explored = [start]
    frontier = [start]
    dfs_path = {}
    iteration = 0

    while len(frontier) > 0:
        iteration += 1
        current_cell = frontier.pop()
        if current_cell == (1, 1):
            break
        for d in 'ESNW':
            if maze.maze_map[current_cell][d]:
                if d == 'E':
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif d == 'S':
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif d == 'N':
                    child_cell = (current_cell[0] - 1, current_cell[1])
                elif d == 'W':
                    child_cell = (current_cell[0], current_cell[1] - 1)
                if child_cell in explored:
                    continue
                explored.append(child_cell)
                frontier.append(child_cell)
                dfs_path[child_cell] = current_cell
    forward_path = {}
    cell = (1, 1)

    while cell != start:
        forward_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]

    return forward_path, iteration