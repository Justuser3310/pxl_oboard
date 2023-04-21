import requests
from time import sleep
from tqdm import tqdm

global xc, yc
xc = 0 ; yc = 0

def draw(cords, color = "black"):
    global xc, yc
    for i in tqdm(range(len(cords))):
        payload = {'x': cords[i][1] + yc, 'y': cords[i][0] + xc, 'color': color }
        
        response = requests.post('http://pb.dmcraft.online', data=payload)
        
        while str(response) != "<Response [200]>":
            response = requests.post('http://pb.dmcraft.online', data=payload)
            print("Error, retrying...")
            sleep(0.1)
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

def fill(xy1, xy2):
    res = []
    for x in range(xy1[0], xy2[0] + 1):
        for y in range(xy1[1], xy2[1] + 1):
            res.append( [x, y] )
    return res




#xc = 500
#yc = 500

draw(fill([26,0], [50, 85]),"white")

'''
#Russian flag
draw(fill([300,300], [330, 300]))
draw(fill([300,330], [330, 330]))
draw(fill([300,300], [300, 330]))
draw(fill([330,300], [330, 330]))

draw(fill([301,321], [329, 329]), "white")
draw(fill([301,310], [329, 320]), "blue")
draw(fill([301,301], [329, 310]), "red")
'''
