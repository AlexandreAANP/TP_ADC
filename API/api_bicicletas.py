from FileReader import FileReader
import os

file = FileReader(os.getcwd()+"/Data/utilizador.json")
for i in file.object_list:
    print(i)

