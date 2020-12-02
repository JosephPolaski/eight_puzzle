"""
verify_puzzle.py 

This module contains the verification algorithim to determine the decision problem for 8-puzzle.
This decision problem asks, if given an 8-puzzle, can it be solved in k moves. In this case the 
k value will be provided by the user. The user may also play the game and see if they are 
able to solve it in k moves.

The approach I took to solving this decision problem was to build a tree out of all possible
moves that could be made at each turn in the game. Then I use a breadth first search (BFS) to find
the shortest path from start to finish. If no 'solved' state for the game is found by k moves 
then the decision problem unsolvable in that amount of turns. if it is solved before or at k turns
then a sequence of moves will be returned that will allow the user to win the game in k turns.
"""
import puzzle_board, queue, copy

class Node:
    """Represents a node in the game move tree"""

    def __init__(self, move_status, prev_move):
        self.status = move_status
        self.generation = 0 # keeps track of which generation of moves the node exists in (k value)
        self.solved = False # changed to true when a solved puzzle is reached
        self.children = []  # will contain pointers to children nodes created by exploring possible moves
        self.parent = None  # pointer to parent of node, used in getting moves list
        self.created_by = prev_move # keeps track of move that created each node so as to not 'undo' the last move or create infinite loop of doing such

    def __repr__(self):
        return "Node Puzzle Status: " + str(self.status.puzzle) + '\n' + "Generation: " + str(self.generation) +'\n'

def build_move_tree(starting_puzzle, k):
    """
    Builds a tree by taking a starting puzzle and
    creating children for each possible move. This will
    always be a value of 2, 3 or 4. This will create a tree of
    maximum height k + 1.

    :param starting_puzzle: this is the puzzle initialized at the beginning of the game
    :return list: [solved = True or False, timeout = True or False, root: root node of tree, solution: solution leaf of tree]
    """
    solved = False # solved flag
    timeout = False # timed out before being solved
    solution = None # pointer to winning node

    already_visited = [] # tracks already visited puzzle move states, this is done to avoid infinite loops where previously visited states are re-created

    creation_queue = queue.Queue()  # create queue to schedule tree node creation/exploration
    
    root = Node(starting_puzzle, None) # create root node

    creation_queue.put(root)    # enqueue root node

    while not creation_queue.empty():

        next_node = creation_queue.get()    # get next node in queue

        # check if the current state was already explored. 
        if next_node.status.puzzle not in already_visited:
            already_visited.append(next_node.status.puzzle) # add to list of explored
        else:
            continue    # already explored skip

        if next_node.solved == True: # check for solved puzzle
            solved = True
            next_node.generation = next_node.parent.generation + 1 # set node generation to parent generation + 1
            solution = next_node
            break

        if solved == False and next_node.generation > k: # check if not solvable in k moves
            timeout = True
            break

        node_children = next_node.status.find_valid_moves()   # determine which moves need to be turned into children

        for move in node_children:  # create a child node for each possible move state

            if move != get_opposite_move(next_node.created_by) and move is not None:

                new_child = Node(copy.deepcopy(next_node.status), move) # give the node a copy of the parent class object and the move that created it

                new_child.status.make_move(move)  # execute move on the child class object within the node to make it reflect the updated move state   

                # if solved update self.solved
                if new_child.status.puzzle == new_child.status.solved:
                    new_child.solved = True            

                new_child.generation = next_node.generation + 1 # set node generation to parent generation + 1

                next_node.children.append(new_child) # add to child list for parent 

                new_child.parent = next_node    # set pointer to parent               

                creation_queue.put(new_child)   # add child to queue                          
        
    return [solved, timeout, root, solution]

def get_solving_moves(solution):
    """Produces a list of moves to solve the puzzle"""

    move_list = []  # holds moves

    current = solution # current node pointer

    while current.parent is not None:   # traverse back along successful move choices
        move_list.append(current.created_by)
        current = current.parent

        move_list.reverse()

    return move_list

def get_opposite_move(move):
    """
    finds opposite of a given move

    :return opposite_move: the opposite of move e.g. up -> down
    """
    if move == 'up':
        return 'down'
    elif move == 'down':
        return 'up'
    elif move == 'left':
        return 'right'
    elif move == 'right':
        return 'left'
    elif move is None:
        return None





    





