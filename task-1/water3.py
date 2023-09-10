def initial_state():
    return (8, 0, 0)

def is_goal(s):
    # goal state: (4,4,0)
    return (s[0] == 4 and s[1] == 4)

def successors(s):
    x, y, z = s

    # pour from x to another
    if (x > 0):
        remain = 5 - y
        if (remain > 0):
            if (x > remain):
                yield ((x-remain, 5, z), remain) # full desc
            else:
                yield ((0, y+x, z), x)           # empty source
        
        remain = 3 - z
        if (remain > 0):
            if (x > remain):
                yield ((x-remain, y, 3), remain)
            else:
                yield ((0, y, z+x), x)
    
    # pour from y to another
    if (y > 0):
        remain = 8 - x
        if (remain > 0):
            if (y > remain):
                yield ((8, y-remain, z), remain)
            else:
                yield ((x+y, 0, z), y)
        
        remain = 3 - z
        if (remain > 0):
            if (y > remain):
                yield ((x, y-remain, 3), remain)
            else:
                yield ((x, 0, z+y), y)

    # pour from z to another
    if (z > 0):
        remain = 8 - x
        if (remain > 0):
            if (z > remain):
                yield ((8, y, z-remain), remain)
            else:
                yield ((x+z, y, 0), z)
        
        remain = 5 - y
        if (remain > 0):
            if (z > remain):
                yield ((x, 5, z-remain), remain)
            else:
                yield ((x, y+z, 0), z)
    

    

