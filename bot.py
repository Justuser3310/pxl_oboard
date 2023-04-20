import requests
from time import sleep

def draw(cords):
    for i in range(len(cords)):
        sleep(0.2)
        try:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': cords[i][2]}
        except:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': "b" }
        
        response = requests.post('http://pb.dmcraft.online', data=payload)
        print(response)
        
        while str(response) != "<Response [200]>":
            response = requests.post('http://pb.dmcraft.online', data=payload)
            print("Retrying...")
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


l = [[48, 100, 'r'], [48, 99, 'r'], [48, 96, 'r'], [48, 91, 'r'], [49, 101, 'r'], [49, 100, 'r'], [49, 99, 'r'], [49, 98, 'r'], [49, 97, 'r'], [49, 96, 'r'], [49, 95, 'r'], [49, 92, 'r'], [49, 91, 'r'], [49, 90, 'r'], [49, 88, 'r'], [50, 106, 'r'], [50, 100, 'r'], [50, 99, 'r'], [50, 96, 'r'], [50, 91, 'r'], [50, 89, 'r'], [50, 88, 'r'], [50, 87, 'r'], [50, 85, 'r'], [51, 107, 'r'], [51, 106, 'r'], [51, 105, 'r'], [51, 88, 'r'], [51, 86, 'r'], [51, 85, 'r'], [51, 84, 'r'], [51, 83, 'r'], [52, 108, 'r'], [52, 107, 'r'], [52, 106, 'r'], [52, 85, 'r'], [52, 84, 'r'], [52, 83, 'r'], [52, 82, 'r'], [52, 79, 'r'], [53, 107, 'r'], [53, 83, 'r'], [53, 80, 'r'], [53, 79, 'r'], [53, 78, 'r'], [54, 110, 'r'], [54, 80, 'r'], [54, 79, 'r'], [54, 78, 'r'], [55, 111, 'r'], [55, 110, 'r'], [55, 109, 'r'], [55, 103, 'r'], [55, 79, 'r'], [56, 110, 'r'], [56, 104, 'r'], [56, 103, 'r'], [56, 102, 'r'], [57, 111, 'r'], [57, 104, 'r'], [57, 103, 'r'], [57, 102, 'r'], [57, 77, 'r'], [58, 112, 'r'], [58, 111, 'r'], [58, 110, 'r'], [58, 103, 'r'], [58, 102, 'r'], [58, 101, 'r'], [58, 91, 'r'], [58, 78, 'r'], [58, 77, 'r'], [58, 76, 'r'], [59, 111, 'r'], [59, 102, 'r'], [59, 101, 'r'], [59, 100, 'r'], [59, 92, 'r'], [59, 91, 'r'], [59, 90, 'r'], [59, 77, 'r'], [59, 76, 'r'], [59, 75, 'r'], [60, 113, 'r'], [60, 102, 'r'], [60, 101, 'r'], [60, 100, 'r'], [60, 94, 'r'], [60, 93, 'r'], [60, 92, 'r'], [60, 91, 'r'], [60, 76, 'r'], [60, 75, 'r'], [61, 114, 'r'], [61, 113, 'r'], [61, 112, 'r'], [61, 101, 'r'], [61, 100, 'r'], [61, 99, 'r'], [61, 95, 'r'], [61, 94, 'r'], [61, 93, 'r'], [61, 92, 'r'], [61, 76, 'r'], [61, 75, 'r'], [61, 74, 'r'], [62, 113, 'r'], [62, 101, 'r'], [62, 100, 'r'], [62, 99, 'r'], [62, 96, 'r'], [62, 95, 'r'], [62, 94, 'r'], [62, 93, 'r'], [62, 75, 'r'], [62, 74, 'r'], [63, 101, 'r'], [63, 100, 'r'], [63, 99, 'r'], [63, 96, 'r'], [63, 95, 'r'], [63, 94, 'r'], [63, 75, 'r'], [63, 74, 'r'], [63, 73, 'r'], [64, 100, 'r'], [64, 99, 'r'], [64, 98, 'r'], [64, 97, 'r'], [64, 96, 'r'], [64, 95, 'r'], [64, 74, 'r'], [65, 101, 'r'], [65, 100, 'r'], [65, 99, 'r'], [65, 98, 'r'], [65, 97, 'r'], [66, 115, 'r'], [66, 114, 'r'], [66, 102, 'r'], [66, 101, 'r'], [66, 100, 'r'], [66, 99, 'r'], [66, 98, 'r'], [66, 97, 'r'], [66, 96, 'r'], [66, 74, 'r'], [67, 116, 'r'], [67, 115, 'r'], [67, 114, 'r'], [67, 113, 'r'], [67, 103, 'r'], [67, 102, 'r'], [67, 101, 'r'], [67, 100, 'r'], [67, 98, 'r'], [67, 97, 'r'], [67, 96, 'r'], [67, 75, 'r'], [67, 74, 'r'], [67, 73, 'r'], [68, 115, 'r'], [68, 114, 'r'], [68, 104, 'r'], [68, 103, 'r'], [68, 102, 'r'], [68, 98, 'r'], [68, 97, 'r'], [68, 96, 'r'], [68, 74, 'r'], [69, 105, 'r'], [69, 104, 'r'], [69, 103, 'r'], [69, 97, 'r'], [69, 96, 'r'], [69, 95, 'r'], [69, 74, 'r'], [70, 115, 'r'], [70, 106, 'r'], [70, 105, 'r'], [70, 104, 'r'], [70, 97, 'r'], [70, 96, 'r'], [70, 95, 'r'], [70, 75, 'r'], [70, 74, 'r'], [70, 73, 'r'], [71, 116, 'r'], [71, 115, 'r'], [71, 114, 'r'], [71, 107, 'r'], [71, 106, 'r'], [71, 105, 'r'], [71, 104, 'r'], [71, 97, 'r'], [71, 96, 'r'], [71, 95, 'r'], [71, 74, 'r'], [72, 115, 'r'], [72, 106, 'r'], [72, 105, 'r'], [72, 104, 'r'], [72, 103, 'r'], [72, 97, 'r'], [72, 96, 'r'], [72, 95, 'r'], [73, 116, 'r'], [73, 115, 'r'], [73, 114, 'r'], [73, 105, 'r'], [73, 104, 'r'], [73, 103, 'r'], [73, 102, 'r'], [73, 101, 'r'], [73, 97, 'r'], [73, 96, 'r'], [73, 95, 'r'], [73, 74, 'r'], [74, 115, 'r'], [74, 103, 'r'], [74, 102, 'r'], [74, 101, 'r'], [74, 100, 'r'], [74, 99, 'r'], [74, 96, 'r'], [74, 95, 'r'], [74, 94, 'r'], [74, 75, 'r'], [74, 74, 'r'], [74, 73, 'r'], [75, 102, 'r'], [75, 101, 'r'], [75, 100, 'r'], [75, 99, 'r'], [75, 98, 'r'], [75, 97, 'r'], [75, 96, 'r'], [75, 95, 'r'], [75, 94, 'r'], [75, 74, 'r'], [76, 115, 'r'], [76, 100, 'r'], [76, 99, 'r'], [76, 98, 'r'], [76, 97, 'r'], [76, 96, 'r'], [76, 95, 'r'], [76, 94, 'r'], [76, 93, 'r'], [77, 116, 'r'], [77, 115, 'r'], [77, 114, 'r'], [77, 98, 'r'], [77, 97, 'r'], [77, 96, 'r'], [77, 95, 'r'], [77, 94, 'r'], [77, 93, 'r'], [77, 92, 'r'], [77, 91, 'r'], [78, 115, 'r'], [78, 95, 'r'], [78, 94, 'r'], [78, 93, 'r'], [78, 92, 'r'], [78, 91, 'r'], [78, 90, 'r'], [78, 89, 'r'], [79, 94, 'r'], [79, 93, 'r'], [79, 92, 'r'], [79, 91, 'r'], [79, 90, 'r'], [79, 89, 'r'], [79, 88, 'r'], [79, 87, 'r'], [79, 86, 'r'], [79, 85, 'r'], [80, 112, 'r'], [80, 93, 'r'], [80, 90, 'r'], [80, 89, 'r'], [80, 88, 'r'], [80, 87, 'r'], [80, 86, 'r'], [80, 85, 'r'], [80, 84, 'r'], [80, 77, 'r'], [81, 113, 'r'], [81, 112, 'r'], [81, 111, 'r'], [81, 88, 'r'], [81, 87, 'r'], [81, 86, 'r'], [81, 85, 'r'], [81, 84, 'r'], [81, 83, 'r'], [81, 78, 'r'], [81, 77, 'r'], [81, 76, 'r'], [82, 112, 'r'], [82, 85, 'r'], [82, 84, 'r'], [82, 78, 'r'], [82, 77, 'r'], [82, 76, 'r'], [83, 80, 'r'], [83, 77, 'r'], [84, 81, 'r'], [84, 80, 'r'], [84, 79, 'r'], [85, 108, 'r'], [85, 80, 'r'], [86, 109, 'r'], [86, 108, 'r'], [86, 107, 'r'], [86, 83, 'r'], [87, 108, 'r'], [87, 84, 'r'], [87, 83, 'r'], [87, 82, 'r'], [88, 104, 'r'], [88, 83, 'r'], [89, 105, 'r'], [89, 104, 'r'], [89, 103, 'r'], [89, 100, 'r'], [89, 92, 'r'], [89, 89, 'r'], [90, 104, 'r'], [90, 101, 'r'], [90, 100, 'r'], [90, 99, 'r'], [90, 97, 'r'], [90, 93, 'r'], [90, 92, 'r'], [90, 91, 'r'], [90, 90, 'r'], [90, 89, 'r'], [90, 88, 'r'], [91, 100, 'r'], [91, 98, 'r'], [91, 97, 'r'], [91, 96, 'r'], [91, 92, 'r'], [91, 89, 'r'], [92, 97, 'r']]

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
