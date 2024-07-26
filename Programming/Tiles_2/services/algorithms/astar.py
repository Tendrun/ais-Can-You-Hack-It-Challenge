# services/algorithms/astar.py
from typing import List
from domain import Puzzle
from services.algorithms.base import IStrategy
from services.puzzle.heuristic import PuzzleHeuristicService
from services.puzzle.constants import (
    HEURISTIC_MANHATTAN_DISTANCE, HEURISTIC_MISPLACED, HEURISTIC_TOTAL, HEURISTIC_OPTIONS,
    ASTAR
)


class AStar(IStrategy):
    heuristic_functions = {
        HEURISTIC_MANHATTAN_DISTANCE: 'heuristic_manhattan_distance',
        HEURISTIC_MISPLACED: 'heuristic_misplaced',
        HEURISTIC_TOTAL: 'heuristic_total'
    }

    def __init__(self, initial_puzzle: Puzzle, heuristic: str = None):
        self.start = initial_puzzle
        self.end_position = Puzzle.generate_end_position(len(initial_puzzle.position))
        self.puzzle_heuristic_service = PuzzleHeuristicService(self.end_position)
        self.heuristic_function = self.heuristic_functions[
            HEURISTIC_TOTAL]  # combined heuristic as default, should work
        self.should_stop = False

        if heuristic:
            if heuristic not in HEURISTIC_OPTIONS:
                raise RuntimeError(f'Invalid Heuristic Function Name. Must be one of {HEURISTIC_OPTIONS}')
            self.heuristic_function = self.heuristic_functions[heuristic]

    def __str__(self):
        return ASTAR

    def solve_puzzle(self) -> List[Puzzle]:
        initial_heuristic = getattr(self.puzzle_heuristic_service, self.heuristic_function)(self.start.position)
        queue = [[initial_heuristic, self.start]]
        expanded = set()
        num_expanded_nodes = 0

        while queue and not self.should_stop:
            current_index = min(range(len(queue)), key=lambda i: queue[i][0])
            current_path = queue.pop(current_index)
            current_heuristic, current_node = current_path[0], current_path[-1]

            if current_node.position == self.end_position:
                self.num_expanded_nodes = num_expanded_nodes
                self.solution = current_path[1:]
                self.get_moves_with_directions(self.solution)
                return self.solution

            if tuple(map(tuple, current_node.position)) in expanded:
                continue

            expanded.add(tuple(map(tuple, current_node.position)))
            num_expanded_nodes += 1

            for move in current_node.get_moves():
                if tuple(map(tuple, move.position)) in expanded:
                    continue

                new_heuristic = self._calculate_new_heuristic(move, current_node)
                new_path = [current_heuristic + new_heuristic] + current_path[1:] + [move]
                queue.append(new_path)

        self.num_expanded_nodes = num_expanded_nodes
        self.solution = []
        return self.solution

    def _calculate_new_heuristic(self, move: Puzzle, end_node: Puzzle) -> int:
        return getattr(self.puzzle_heuristic_service, self.heuristic_function)(move.position) - \
            getattr(self.puzzle_heuristic_service, self.heuristic_function)(end_node.position)

    def stop(self):
        self.should_stop = True

    def get_moves_with_directions(self, nodes):

        iteration = 0
        nodeOld = [[]]
        moves = ""

        for nodeNew in nodes:
            print(iteration)
            print("Node Old = ", nodeOld)
            print("Node New = ", nodeNew)

            nodeNewX = 0
            nodeNewY = 0

            nodeNewPos = nodeNew.get_position()
            for i in range(len(nodeNewPos)):
                for j in range(len(nodeNewPos[i])):
                    if nodeNewPos[i][j] == 0:
                        nodeNewX = j
                        nodeNewY = i
                        break

            nodeOldX = 0
            nodeOldY = 0

            if iteration != 0:
                nodeOldPos = nodeOld.get_position()
                for i in range(len(nodeOldPos)):
                    for j in range(len(nodeOldPos)):
                        if nodeOldPos[j][i] == 0:
                            nodeOldX = i
                            nodeOldY = j
                            break

            print("nodeOldX ", nodeOldX)
            print("nodeOldY ", nodeOldY)

            print("nodeNewX ", nodeNewX)
            print("nodeNewY ", nodeNewY)

            if iteration == 0:  #skip first iteration
                pass
            elif nodeOldY > nodeNewY:  # Up
                moves += "U,"
            elif nodeOldY < nodeNewY:  # Down
                moves += "D,"
            elif nodeOldX > nodeNewX:  # Left
                moves += "L,"
            elif nodeOldX < nodeNewX:  # Right
                moves += "R,"

            nodeOld = nodeNew
            iteration += 1
            print(moves)
