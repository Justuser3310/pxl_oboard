import requests
from time import sleep

def draw(cords):
    for i in range(len(cords)):
        sleep(0.2)
        try:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': cords[i][2]}
        except:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': "blue" }
        
        response = requests.post('http://pb.dmcraft.online', data=payload)
        print(response)
        
        while str(response) != "<Response [200]>":
            response = requests.post('http://pb.dmcraft.online', data=payload)
            print("Retrying...")
            print(response)
    print("DONE!")

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


l = [[65, 86, 'red'], [66, 87, 'red'], [66, 86, 'red'], [66, 85, 'red'], [67, 86, 'red'], [89, 97, 'red'], [90, 98, 'red'], [90, 97, 'red'], [90, 96, 'red'], [91, 97, 'red'], [95, 77, 'black'], [96, 78, 'black'], [96, 77, 'black'], [96, 76, 'black'], [97, 77, 'black'], [107, 108, 'blue'], [108, 109, 'blue'], [108, 108, 'blue'], [108, 107, 'blue'], [109, 108, 'blue']]

draw(l)


#draw( liney(300, 300, 500) )
#draw(linex(500, 300, 500))

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
