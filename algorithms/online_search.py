from core.puzzle import get_neighbors
from core.config import goal_state

def copy_state(state):
    return [row[:] for row in state]

def get_state_tuple(state):
    return tuple(tuple(row) for row in state)


def online_search_8_puzzle(start_state):

    def copy_state(state):
        return [row[:] for row in state]

    def get_state_tuple(state):
        return tuple(tuple(row) for row in state)

    s = start_state
    path = [copy_state(s)]
    visited = {get_state_tuple(s)}
    untried = {get_state_tuple(s): get_neighbors(s)}
    unbacktracked = {get_state_tuple(s): []}

    while True:
        if s == goal_state:
            return path

        s_tuple = get_state_tuple(s)
        if s_tuple not in untried:
            untried[s_tuple] = get_neighbors(s)

        while untried[s_tuple]:
            next_s = untried[s_tuple].pop(0)
            next_s_tuple = get_state_tuple(next_s)
            if next_s_tuple not in visited:
                visited.add(next_s_tuple)
                if s_tuple not in unbacktracked:
                    unbacktracked[s_tuple] = []
                unbacktracked[s_tuple].append(copy_state(s))
                s = next_s
                path.append(copy_state(s))
                break
        else:
            if not unbacktracked[s_tuple]:
                return None  # No solution
            else:
                s = unbacktracked[s_tuple].pop()
                path.append(copy_state(s))
