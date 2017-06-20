# -*- coding: utf-8 -*-
'''
将脚本绑定到快捷键（如ctrl+shift+alt+S），快速导出模型到原文件夹并覆盖原文件保存。
'''
import os
import c4d
from c4d import documents



def main():
    # 获取文件路径与文件名    
    doc = documents.GetActiveDocument()
    name = doc.GetDocumentName()
    originPath = doc.GetDocumentPath()
    originFilePath = os.path.join(originPath, name)
    originFilePath = os.path.normpath(originFilePath)

    if doc.SearchObject("FileSaver"):
        fileSaver = doc.SearchObject("FileSaver")
    else:
        print "You need to run 'createSaveOutUserData.py' first"
        return

    isOutputFbx = fileSaver[c4d.ID_USERDATA, 1]
    isSavingOriginFile = fileSaver[c4d.ID_USERDATA, 2]
    filepath = fileSaver[c4d.ID_USERDATA, 3]

    if isOutputFbx:
        if len(filepath) == 0:
            print "You need to specify the file path"
            return

    filepath = os.path.normpath(filepath)
    filepath = "/".join(filepath.split("\\")[:-1])
    # 将文件后缀改为.fbx
    if name[-3:] != "fbx":
        if len(name.split(".")) == 1:
            name = name + ".fbx"
        else:
            index = -1
            while name[index] != '.':
                index -= 1 
            name = name[:(index+1)]+"fbx"
            print "convert filetype to .fbx"
    
    filepath = os.path.join(filepath,name)
    filepath = os.path.normpath(filepath)

    # 导出模型到原文件路径
    if documents.SaveDocument(doc,filepath,c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST,1026370):
        print "export document to: " + filepath
    else:
        print "export failed"

    if isSavingOriginFile:
        if documents.SaveDocument(doc,originFilePath,c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST,c4d.FORMAT_C4DEXPORT):
            print "save origin file to: " + originFilePath
        else:
            print "save origin file failed"

    c4d.EventAdd() 


'''
    op = {}
    
    if plugin.Message(c4d.MSG_RETRIEVEPRIVATEDATA, op):
        fbxExport = op["imexporter"]
        for i in range(1000,2000):
            print fbxExport[i]
        print fbxExport[c4d.OBJEXPORTOPTIONS_TEXTURECOORDINATES]
        if documents.SaveDocument(doc,path,c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST,1026370): #Exports using the FBX exporter
            print "export document to: " + path
        else:
            print "export failed"

        c4d.EventAdd()
'''    
if __name__=='__main__':
    main()
