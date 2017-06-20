import c4d
from c4d import documents

def main():
    doc = documents.GetActiveDocument()
    fileSaver = c4d.BaseObject(c4d.Onull)
    fileSaver.InsertBefore(doc.GetFirstObject())

    fileSaver.SetName("FileSaver")
    
    isOutputFbxFile = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BOOL) # Create default container
    isOutputFbxFile[c4d.DESC_NAME] = "isOutputFbxFile"     
    isOutputFbxFileElement = fileSaver.AddUserData(isOutputFbxFile)
    fileSaver[isOutputFbxFileElement] = True

    isSaveOriginFile = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BOOL) # Create default container
    isSaveOriginFile[c4d.DESC_NAME] = "isSaveOriginFile"     
    isSaveOriginFileElement = fileSaver.AddUserData(isSaveOriginFile)
    fileSaver[isSaveOriginFileElement] = True

    saveOutPath = c4d.GetCustomDataTypeDefault(c4d.DTYPE_FILENAME) # Create default container
    saveOutPath[c4d.DESC_NAME] = "SaveOutPath" 
    fileSaver.AddUserData(saveOutPath)

    c4d.EventAdd()

if __name__ == "__main__":
    main()