import os
import numpy as np
import pickle
import cv2
import random

# get the names
def get_name(line):
    last = False
    ret = ''
    for i in list(line[1:]):
        if i == "<":
            last = False
            break
        if i == ">" and last == False:
            last = True
        elif last == True:
            ret += i
    return ret


class Readxml:
    def __init__(self, dir):
        self.dir = dir

    def list_path(self):
        files = []
        for i in range(500):
            files.append("PartA_" + str(i).zfill(5) + ".xml")
        return files

    def get_data(self):
        data = []
        files = self.list_path()
        for file in files:
            if file[-4:] == ".xml":
                picture = self.read_file(file)
                data.append(picture)
        return data
    # read the information inside the xml file
    def read_file(self, filename):
        filepath = self.dir + filename
        file = open(filepath, "r")
        lines = file.readlines()
        objects, ob = [], []
        l = ["<filename>", "<width>", "<height>", "<depth>",
             "<name>", "<xmin>", "<ymin>", "<xmax>", "<ymax>"]
        picture = {'filename': None, 'size': [None, None, None], 'objects': []}
        for line in lines:
            line = line.strip()
            if "<filename>" in line:
                picture['filename'] = filename
            elif "<width>" in line:
                picture["size"][0] = get_name(line)
            elif "<height>" in line:
                picture["size"][1] = get_name(line)
            elif "<depth>" in line:
                picture["size"][2] = get_name(line)
            elif "<name>" in line:
                ob.append('person')
            elif "<xmin>" in line:
                ob.append(get_name(line))
            elif "<ymin>" in line:
                ob.append(get_name(line))
            elif "<xmax>" in line:
                ob.append(get_name(line))
            elif "<ymax>" in line:
                ob.append(get_name(line))
            if len(ob) == 5:
                objects.append(ob)
                ob = []
        picture["objects"] = objects
        return picture
    # write the data to csv
    def write_to_csv(self, write2):
        data = self.get_data()
        csv = {"filename": [], "size": [], "objects": []}
        for picture in data:
            csv["filename"].append(picture["filename"])
            csv["size"].append(picture["size"])
            csv["objects"].append(picture["objects"])
        return csv


if __name__ == "__main__":
    read = Readxml("./data/marks/")
    data = read.write_to_csv("./data/data.pickle")
    # free image is the group of images that do not contains head at all
    def free_image(size, positions):
        ret = []
        x = list(map(lambda x: x*64,list(range(int(int(size[0])/64)))))
        y = list(map(lambda x: x*64,list(range(int(int(size[1])/64)))))
        for i in range(1, len(x)):
            for j in range(1, len(y)):
                for position in positions:
                    xmin, xmax, ymin, ymax = int(position[1]), int(position[3]), int(position[2]), int(position[4])
                    if x[i-1] < xmin < x[i] and y[j-1] < ymin < y[j]:
                        break
                    if x[i-1] < xmin < x[i] and y[j-1] < ymax < y[j]:
                        break
                    if x[i-1] < xmax < x[i] and y[j-1] < ymin < y[j]:
                        break
                    if x[i-1] < xmax < x[i] and y[j-1] < ymax < y[j]:
                        break
                    l = [x[i-1], y[j-1], x[i], y[j]]
                    if l not in ret:
                        ret.append(l)
        return ret
    # get the pictures containing heads and the pictures do not contain any head
    def pre_process(num,impath,data):
        sizes = data["size"]
        positions = data["objects"]
        pictures, free = [], []
        for i in range(num,impath):
            position = positions[i]
            size = sizes[i]
            free_location = free_image(size, position)
            img = cv2.imread(impath + str(i).zfill(5) + ".jpg")
            for p in position:
                xmin, xmax, ymin, ymax = int(p[1]), int(p[3]), int(p[2]), int(p[4])
                if xmin > xmax:
                    xmin, xmax = xmax, xmin
                if ymin > ymax:
                    ymin, ymax = ymax, ymin
                pictures.append(img[ymin:ymax, xmin:xmax])

            for p2 in free_location:
                if len(p2) == 4:
                    xmin, xmax, ymin, ymax = int(p2[0]), int(p2[2]), int(p2[1]), int(p2[3])
                free.append(img[ymin:ymax, xmin:xmax])

            for i in pictures:
                i = np.array(cv2.resize(i, (64, 64)))
                cv2.imwrite("./data/people/{0}.png".format(j),i)
                j+=1

            for j in range(10000):
                num = random.randint(0,54000)
                i = free[num]
                i = np.array(cv2.resize(i, (64, 64)))
                cv2.imwrite("./data/others/{0}.png".format(j),i)
            return pictures,free

    pictures,free = pre_process(500,"./data/image/PartA_",data)

    label_1 = list(np.ones(len(pictures)))
    label_2 = list(np.zeros(len(free)))
    data["picture"] = pictures
    data["free_image"] = free
    data["positive"] = label_1
    data["negative"] = label_2
    # store the data
    with open("./data/data.pickle", "wb") as file:
        pickle.dump(data, file)
        file.close()
