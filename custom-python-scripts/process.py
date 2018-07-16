#dx,dy,d(theta)

import math

def sumtill(oblu, whose, till):
    count = 0
    for i in range (till+1):
        count += dict_log[i][oblu-1][whose]
    return count


def total_theta(oblu, number):
    theta = 0
    for i in range (number+1):
        theta += dict_log[i][oblu-1][3]
    return theta

def totalof(oblu, whose, number):
    v = 0
    if whose==0:
        for i in range (number+1):
            v += dict_log[i][oblu-1][4]*math.sin(total_theta(oblu, i))
    else:
        for i in range (number+1):
            for i in range (number+1):
              v += dict_log[i][oblu-1][4]*math.cos(total_theta(oblu, i))
    return v


dict_log={0: [[1, 2, 3, 4,2], [1.3, 2, 3, 4,2]], 1: [[1, 2, 3, 4,2], [1, 2, 3, -4,2]], 2: [[1, 2, 3, 4,2], [1, 2, 3, 4.7,2]]}

print totalof(2,0,2)
