import math

def main(y):
    if(y < 62):
        return 99 * y**2 - 66 * y**5
    elif(y < 94 and y >= 62):
        return math.cos(y)**3 / 50 + 63 * \
               math.atan(70 * y + 27 * y**3) + y**6
    else:
        return math.tan(1 - 97 * y - 76 * y**2)**5 + \
               (y**3 - 1)**6 + math.tan(y)**2

