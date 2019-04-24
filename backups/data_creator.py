import numpy as np
import matplotlib.pyplot as plt
import pickle
from random import randint,random
time_moving = 2
time_stop = 10
# generate data pares current level and my level(going up)
def generate_up(current_level,my_level):
    number = randint(current_level,my_level)
    l = []
    a = current_level+1
    for i in range(number):
        if a<my_level - 1:
            a = randint(a,my_level-1)
            if a in l:
                a= randint(a,my_level -1)
            else:
                l.append(a)
    return l
# generate level (going down)
def generate_down(current_level,my_level):
    number = randint(my_level,current_level)
    l = []
    a = current_level - 1
    for i in range(number):
        if a>my_level + 1:
            a = randint(my_level + 1, a)
            while a in l:
                a= randint(my_level + 1,a)
            else:
                l.append(a)
    return l
# define the time need 
def time(l):
    start, end, levels = l
    stops = len(levels)
    time = 16 + stops*10 + 2*abs(end-start)
    error = random() + randint(-2,2)
    ret = time + round(error,2)
    return ret

data = []
# generate a group of data that need to use
for i in range(100):
    current_level,my_level = randint(1,12),randint(1,12)
    while current_level == my_level:
        current_level, my_level = randint(1, 12), randint(1, 12)
    if current_level > my_level:
        current_level,my_level = my_level,current_level
    data.append([current_level,my_level,generate_up(current_level,my_level)])

for i in range(100):
    current_level,my_level = randint(1,12),randint(1,12)
    while current_level == my_level:
        current_level, my_level = randint(1, 12), randint(1, 12)
    if current_level < my_level:
        current_level,my_level = my_level,current_level
    data.append([current_level,my_level,generate_down(current_level,my_level)])

x = []
y=[]
for i in data:
    if len(i)==3:
        y.append(time(i))
        x.append(i)
d= {"x":x,"y":y}

plt.plot(y)
plt.show()
file = open("train_data.pickle","wb")
pickle.dump(d,file)
file.close()
