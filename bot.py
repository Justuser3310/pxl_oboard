import requests
from time import sleep
from tqdm import tqdm

def draw(cords):
    for i in tqdm(range(len(cords))):
        sleep(0.2)
        try:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': cords[i][2]}
        except:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': "blue" }
        
        response = requests.post('http://pb.dmcraft.online', data=payload)
        #print(response)
        
        while str(response) != "<Response [200]>":
            response = requests.post('http://pb.dmcraft.online', data=payload)
            print("Error, retrying...")
            #print(response)
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

draw(fill([14,14], [26,26]))


