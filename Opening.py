import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)
import csv


def get_arrays(path):
    data = open(path, 'r')
    data = csv.reader(data)
    result = []
    for ro in data:
        result.append((int(ro[0]), np.array(ro[1:], dtype=float)))
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


