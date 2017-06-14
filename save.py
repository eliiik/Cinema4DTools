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
    path = doc.GetDocumentPath()
    name = doc.GetDocumentName()
    # 将文件后缀改为.fbx
    if name[-3:] != "fbx":
        try:
            index = -1
            while name[index] != '.':
                index -= 1 
            name = name[:(index+1)]+"fbx"
            print "convert filetype to .fbx"
        except IndexError:
            print "maybe you need to save your file first"
            return
    
    path = os.path.join(path,name)
    # 导出模型到原文件路径
    if documents.SaveDocument(doc,path,c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST,1026370):
        print "export document to: " + path
    else:
        print "export failed"

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
