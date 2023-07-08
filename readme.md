This project is to implement a number of search and MDP algorithms and compare their performance in a maze search.

All code is in the folder ai_assignment1, please unzip it and place in a suitable place.

pip install pyamaze #install pyamaze

run below command to see different method solving different size of maze, supported MazeSize 10x10, 30x30, 50x50.

python performance_comparison.py --MazeSize 50x50 --Method dfs
python performance_comparison.py --MazeSize 50x50 --Method bfs
python performance_comparison.py --MazeSize 50x50 --Method astar
python performance_comparison.py --MazeSize 50x50 --Method mdp_value
python performance_comparison.py --MazeSize 50x50 --Method mdp_policy
