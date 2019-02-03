import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)
import csv
from Utils import *


def get_from_txt(path):
    file = open(path, 'r')
    f1 = file.readlines()
    result = []
    for i in f1:
        #print(i)
        akbar = i.split(" ")
        akbar = [float(akbar[0]), float(akbar[1])]
        akbar = np.array(akbar, dtype=float)
        # print(akbar)
        #b = list(i)
        #print(b)
        result.append(akbar)
    return result


def get_arrays(path):
    fpath = 'data_f.txt'
    data = open(path, 'r')
    data = csv.reader(data)
    feature = get_from_txt(fpath)
    result = []
    for ro in data:
        result.append((int(ro[0]), np.array(ro[1:], dtype=float)))
    # for i in range(len(result)):
    #     result[i] = (result[i][0], np.append(result[i][1], has_closed(result[i][1])))
    #     print(i)
    #print('compeleted saving the shit')
    for i in range(len(result)):
        result[i] = (result[i][0], np.append(result[i][1], feature[i]))
    return result


def show_picture(in_array):
    A = in_array.reshape((28, 28))
    A = np.matrix(A)
    plt.style.use('classic')
    plt.imshow(A, cmap='gray')
    title = "Original Image"
    plt.title(title)
    plt.draw()
    plt.show()

def save_pic(arr, name):
    arr = arr.reshape((28, 28))
    arr = np.matrix(arr)
    plt.style.use('classic')
    plt.imshow(arr, cmap='gray')
    title = "Original Image"
    plt.title(title)
    plt.draw()
    plt.savefig(name)
    plt.show()

if __name__ == '__main__':

    data = get_arrays('data.csv')
    for i in data:
        show_picture(i[1])
    # for row in data:
    #     A = np.array(row[1:], dtype='float')
    #     A = A.reshape((28, 28))
    #     A = np.matrix(A)
    #     name = "Images/" + str(i)
    #     i+= 1
    #     # print(A)
    #     # break
    #     plt.style.use('classic')
    #     plt.imshow(A, cmap='gray')
    #     title = "Original Image"
    #     plt.title(title)
    #     plt.draw()
    #     plt.savefig(name)
    #     plt.show()


