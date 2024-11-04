import os
import time

class ImageFile:
    def __init__(self, name, ctime):
        self.name = name
        self.ctime = ctime

    def name(self):
        return self.name

    def ctime1(self):
        return self.ctime

filelist = []
files = os.listdir("/opt/drawio")
for file in files:
    file_path = os.path.join("/opt/drawio/", file)
    if os.path.isfile(file_path):
        file_creation_time = os.path.getctime(file_path)
        fctime = time.ctime(file_creation_time)
        imgFile = ImageFile(file_path, int(file_creation_time)) 
        filelist.append(imgFile)
        print(file_path, type(file), int(file_creation_time * 1000))

print(len(filelist), type(filelist))

for img in filelist:
    print('img', type(img), img.name)

to_copy_list = list(filter(lambda img: img.ctime > 1, filelist))

