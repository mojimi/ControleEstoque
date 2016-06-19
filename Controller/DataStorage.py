import pickle
class DataStorage:
    file_Name = "dataBase.txt"

    def __init__(self):
        self.file_Name = "dataBase.txt"

    def storageData(self, data):
        fileObject = open(self.file_Name, 'wb')
        pickle.dump(data,fileObject)
        fileObject.close()

    def readData(self):
        fileObject = open(self.file_Name,'r')
        pickle.load(fileObject)
        fileObject.close()
