# -*- coding: utf-8 -*-
'''

'''
import os
import c4d
from c4d import documents
from c4d import utils
from c4d import storage

def main():

    # Get file data  
    document = documents.GetActiveDocument()
    path = document.GetDocumentPath()
    name = document.GetDocumentName()
    settings = c4d.BaseContainer()

    obj = document.SearchObject("Connect")
    userDataObject = document.SearchObject("Mordifier")
    objList = document.GetObjects()

    outPutFilename = userDataObject[c4d.ID_USERDATA, 15]
    outPutPath = userDataObject[c4d.ID_USERDATA, 16]

    # C-Model
    return_value = utils.SendModelingCommand(
        command = c4d.MCOMMAND_CURRENTSTATETOOBJECT,
        list = [obj],
        mode=c4d.MODELINGCOMMANDMODE_ALL,
        bc=settings,
        doc = document)

    if return_value:
        document.InsertObject(return_value[0]) #return_value is a list in this case
        c4d.EventAdd()
    
    # del others
    for i in objList:
        i.Remove()

    # change name of the model
    newModel = document.GetFirstObject()
    newModel.SetName(outPutFilename)
        
    # delete all material
    mat = document.GetMaterials()
    for i in mat:
        i.Remove()

    # save file
    # path = "C:\\newStart\\Assets\\Models\\CutOutModels\\"
    name = outPutFilename + "_forUnity.c4d"
    path = os.path.join(outPutPath,name)
    # 导出模型到原文件路径
    if documents.SaveDocument(doc,path,c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST,
c4d.FORMAT_C4DEXPORT):
        print "export document to: " + path
    else:
        print "export failed"
    
    # open new model
#     try:
#          newDoc = documents.LoadDocument(path, c4d.
# SCENEFILTER_0)
#     except IOError:
#         print "Can't open the new model"

    c4d.EventAdd() 

if __name__=='__main__':
    main()
