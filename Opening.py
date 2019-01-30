import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)
import csv

if __name__ == '__main__':
    data = open('data.csv', 'r')
    data = csv.reader(data)
    i = 0;
    for ro in data:
        i += 1
    print(i)

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



