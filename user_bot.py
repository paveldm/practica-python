#def script(check, x, y):
 #   if check("level") == 1:
  #      return "right"
   # return "pass"


def script(check, x, y):
    if check("gold", x, y):
        return "take"

    if check("level") == 1:
        if not check("wall", x + 2, y):
            return "right"
        return "down"

    if check("level") == 2:
        if check("gold", x-1,y):
            return "left"
        if check("gold",x,y+1):
            return "down"
        if check("gold",x,y-1):
            return "up"
        if check("wall",x+1,y):
            return "up"
        if check("wall",x,y-1):
            return "right"
        if check("wall",x,y+1):
            return "right"

    if check("level") == 3:
        if check("wall", x - 1, y):
            if not check("wall", x, y - 1):
                return "up"
        if check("wall", x + 1, y):
            if not check("wall", x, y + 1):
                return "down"
        if check("wall", x, y - 1):
            if not check("wall", x + 1, y):
                return "right"
        if check("wall", x, y + 1):
            if not check("wall", x - 1, y):
                return "left"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x + 1, y + 1):
            return "down"
        if check("wall", x - 1, y + 1):
            return "left"

    if check("level") == 4:
        if x == 4 and y == 13:
            return "right"
        if x == 7 and 12 <= y <= 13:
            return "up"
        if check("wall", x - 1, y):
            if not check("wall", x, y - 1):
                return "up"
        if check("wall", x + 1, y):
            if not check("wall", x, y + 1):
                return "down"
        if check("wall", x, y - 1):
            if not check("wall", x + 1, y):
                return "right"
        if check("wall", x, y + 1):
            if not check("wall", x - 1, y):
                return "left"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x + 1, y + 1):
            return "down"
        if check("wall", x - 1, y + 1):
            return "left"