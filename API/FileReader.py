import json

class FileReader:
    data = None
    data_type = None
    object_list = []
    def __init__(self, path :str):
        self.data = json.loads(open(path).read())
        self.data_type = list(self.data.keys())[0]


    def readTest():    
        for object_data in self.data[self.data_type]:
            
                