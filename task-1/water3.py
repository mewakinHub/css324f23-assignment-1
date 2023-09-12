def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s # unpacking
    # # Try to empty one bottle
    # if x > 0:
    #     yield ((0,y,z), x)
    # if y > 0:
    #     yield ((x,0,z), y)
    # if z > 0:
    #     yield ((x,y,0), z)
    # # Try to fill up one bottle
    # if x < 8:
    #     yield ((8,y,z), 8-x)
    # if y < 5:
    #     yield ((x,5,z), 5-y)
    # if z < 3:
    #     yield ((x,y,3), 3-z)
    # Actions: pour water from one bottle to another bottle. However, you can only pour until the source bottle is empty or until the destination bottle is full.
    # Try to pour from one to another
    # transfer(max - current)
    # Pour to 3L
    t = 3 - z
    # 8L to 3L
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t, y, 3), t)
        else:
            yield ((0, y, z+x), x)
    # 5L to 3L
    if y > 0 and t > 0:
        if y > t:
            yield ((x, y-t, 3), t)
        else:
            yield ((x, 0, z+y), y)
    # Pour to 5L
    t = 5 - y 
    # 8L to 5L
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t, 5, z), t)
        else:
            yield ((0, y+x, z), x)
    # 3L to 5L
    if z > 0 and t > 0:
        if z > t:
            yield ((x, 5, z-t), t)
        else:
            yield ((x, y+z, 0), z)
    # Pour to 8L
    t = 8 - x
    # 5L to 8L
    if y > 0 and t > 0:
        if y > t:
            yield ((8, y-t, z), t)
        else:
            yield ((x+t, 0, z), y)
    # 3L to 8L
    if z > 0 and t > 0:
        if z > t:
            yield ((8, y, z-t), t)
        else:
            yield ((x+z, y, 0), z)