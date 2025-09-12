def simulate(prog, xsize, ysize):
    """Given a "program" *prog*, run that program by "moving around" and
    tracking what happens. Use a set of tuples to track locations visited.

    Return the number of junctions visited and the number of
    time-steps used.
    A junction is defined as a the current_direction != last_direction
    Examples of usage and results:

    >>> simulate("NNN", 100, 100)
    (4, 3)
    >>> simulate("NNNSSS", 100, 100)
    (4, 6)
    >>> simulate("NNNESSS", 100, 100)
    (8, 7)
    >>> simulate("NNNNNSSSSS", 3, 3) # will actually take 2 steps north and 2 south => total 4 time-steps
    (3, 4)
    """
    
    grid = [[0 for _ in range(xsize)] for _ in range(ysize)]
    pos: tuple[int, int] = (0,0)
    junctions_visited:set[tuple[int,int]]={pos}
    time_step = 0
    direction_dict ={"N": (1,0), "S": (-1,0), "E": (0,1), "W": (0,-1)}
    
    grid[pos[0]][pos[1]] = 1
    for current_dir in prog:
        if current_dir not in direction_dict:
            raise Exception("Illegal args")
        direction = direction_dict[current_dir]
        new_x, new_y = pos[0] + direction[0], pos[1] + direction[1]
        if  new_x < xsize and new_y < ysize :
            pos = (new_x, new_y)
            grid[pos[0]][pos[1]] = 1
            junctions_visited.add(pos)
            time_step += 1

    return len(junctions_visited), time_step 
import doctest
doctest.run_docstring_examples(simulate, globals(), verbose=True)
