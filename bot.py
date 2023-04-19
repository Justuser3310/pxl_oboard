import requests
from time import sleep

def draw(cords):
    for i in range(len(cords)):
        sleep(0.6)

        payload = {'x': cords[i][1], 'y': cords[i][0], 'color': 'b'}
        response = requests.post('http://pb.dmcraft.online', data=payload)
        print(response)

def linex(y, x1, x2):
    res = []
    for i in range(x1, x2+1):
        res.append( [i,y] )
    return res

def liney(x, y1, y2):
    res = []
    for i in range(y1, y2+1):
            res.append( [x,i] )
    return res


#draw( liney(300, 300, 500) )
draw(linex(500, 300, 500))

'''
xs = 180
ys = 180
#S
cords = [ [3+xs,0+ys],[2+xs,0+ys],[1+xs,0+ys],[1+xs,-1+ys],[1+xs,-2+ys],[2+xs,-2+ys],[3+xs,-2+ys],[3+xs,-3+ys],[3+xs,-4+ys],[2+xs,-4+ys],[1+xs,-4+ys] ]
draw(cords)
#A
cords = [ [5+xs,-4+ys],[5+xs,-3+ys],[5+xs,-2+ys],[5+xs,-1+ys],[5+xs,0+ys],[6+xs,0+ys],[7+xs,0+ys],[8+xs,0+ys],[8+xs,-4+ys],[8+xs,-3+ys],[8+xs,-2+ys],[8+xs,-1+ys],[8+xs,0+ys],[5+xs,-2+ys],[6+xs,-2+ys],[7+xs,-2+ys],[8+xs,-2+ys], ]                           
draw(cords)
#N
cords = [ [10+xs,-4+ys],[10+xs,-3+ys],[10+xs,-2+ys],[10+xs,-1+ys],[10+xs,0+ys],[11+xs,-1+ys],[12+xs,-2+ys],[13+xs,-3+ys],[14+xs,-4+ys],[15+xs,-4+ys],[15+xs,-3+ys],[15+xs,-2+ys],[15+xs,-1+ys],[15+xs,0+ys], ]
draw(cords)
#S
xs = xs + 16
cords = [ [3+xs,0+ys],[2+xs,0+ys],[1+xs,0+ys],[1+xs,-1+ys],[1+xs,-2+ys],[2+xs,-2+ys],[3+xs,-2+ys],[3+xs,-3+ys],[3+xs,-4+ys],[2+xs,-4+ys],[1+xs,-4+ys] ]
draw(cords)
'''
