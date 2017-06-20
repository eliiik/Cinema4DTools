import c4d
#Welcome to the world of Python
document = c4d.documents.GetActiveDocument()

obj = op.GetMain()

def main():
    
    maxY = 0.0
    
    if obj.GetChildren():
        children = obj.GetChildren()
        for i in children:
            if i.GetAbsPos().y > maxY:
                maxY = i.GetAbsPos().y
    
    obj[c4d.ID_USERDATA,1] = maxY
