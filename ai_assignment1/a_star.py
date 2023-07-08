from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze):
    start = (maze.rows, maze.cols)
    a_path = {}
    search_path = [start]
    g_score = {cell: float('inf') for cell in maze.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in maze.grid}
    f_score[start] = g_score[start] + h(start, (1, 1))
    # f_score[start] = h(start, (1, 1))
    open = PriorityQueue()
    open.put((f_score[start], h(start, (1, 1)), start))
    # open.put((h(start, (1, 1)), h(start, (1, 1)), start))
    iteration = 0
    while not open.empty():
        iteration += 1
        current_cell = open.get()[2]
        search_path.append(current_cell)
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

                temp_g_score = g_score[current_cell] + 1
                temp_f_score = temp_g_score + h(child_cell,(1,1))

                if temp_f_score < f_score[child_cell]:
                    f_score[child_cell] = temp_f_score
                    g_score[child_cell] = temp_g_score
                    open.put((f_score[child_cell],h(child_cell,(1,1)),child_cell))
                    a_path[child_cell] = current_cell

    forward_path = {}
    cell = (1, 1)
    while cell != start:
        forward_path[a_path[cell]] = cell
        cell = a_path[cell]

    return search_path, a_path, forward_path, iteration

