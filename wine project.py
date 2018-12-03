import csv
import numpy as np

with open ('C:/Users/Serkan/PycharmProjects/panda/scipy-lecture-notes-2017.1.1/data/winequality-red.csv', 'r') as f:
    wines = list(csv.reader(f,delimiter=';'))
quantities = [float(item[-1]) for item in wines[1:]]

d = sum(quantities)/len(quantities)
wines = np.array(wines[1:], dtype=np.float)

#we read the file and inserted it into anumpy array

#read array from txt

wine = np.genfromtxt("C:/Users/Serkan/PycharmProjects/panda/scipy-lecture-notes-2017.1.1/data/winequality-red.csv", delimiter=";",skip_header=1)



third_wine = wines[3,:]

