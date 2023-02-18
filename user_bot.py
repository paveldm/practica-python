﻿#def script(check, x, y):
 #   if check("level") == 1:
  #      return "right"
   # return "pass"


def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y):
            return "take"
        if check("wall", x+2, y):
            return "down"
        else:
            return "right"


    if check("level") == 2:
        if check("gold", x, y):
            return "take"
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
        if not(check("wall",x, y+1)):
            return "up"
        elif check("wall", x, y+1):
            return "right"