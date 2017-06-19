import c4d
from c4d.modules import mograph as mo
#Welcome to the world of Python

flag = 1
isFirst = 1
obj = op.GetObject()


def main():
    global flag
    global isFirst
    global pointSave
    
    isUpdate = obj[c4d.ID_USERDATA, 1]
    curve = obj[c4d.ID_USERDATA, 2]
    if isUpdate:
        if isFirst:
            pointSave = curve.GetAllPoints()
            isFirst = 0
            
        allPoints = curve.GetAllPoints()
        
        if sum(allPoints) == sum(pointSave):
            pass
        
        else:
            pointSave = allPoints
            obj[c4d.MG_POLYSURFACE_COUNT] += flag
            if flag > 0:
                flag = -1
            else:
                flag = 1
                
    else:
        pass
        

