import pickle
import os.path


class DataStorage:

    def __init__(self):
        self.file_Name = "dataBase.txt"

    def save(self, data):
        try:
            with open(self.file_Name, "wb") as myData:
                pickle.dump(data,myData)
                myData.close()
        except pickle.PickleError as err:
            print(str(err))

    def load(self):
        try:
            if os.path.isfile(self.file_Name):
                with open(self.file_Name,'rb') as myData:
                    return pickle.load(myData)
            else:
                return []
        except pickle.PickleError as err:
            print(str(err))