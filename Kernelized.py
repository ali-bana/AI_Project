import numpy as np
from Opening import *
from Utils import *


def kernel(data):
    alphas = []
    for i in range(10):
        alphas.append([0 for _ in range(len(data))])
    for i in range(len(data)):
        answer = decide(data[i][1], alphas, data[:i])
        if data[i][0] != answer:
            alphas[answer][i] -= 1
            alphas[data[i][0]][i] += 1

    return alphas





def decide(vector, alphas, data):
    scores = [0 for _ in range(10)]
    for i in range(len(alphas)):
        sum = 0
        for j in range(len(data)):
            sum += ((np.dot(vector, data[j][1]) + 1) ** 2) * alphas[i][j]
        scores[i] = sum

    result = 0
    for i in range(len(scores)):
        if scores[i] > scores[result]:
            result = i

    return result



if __name__ == "__main__":
    data = get_arrays('data.csv')
    data = data[0:2000]
    for i in range(len(data)):
        data[i] = (data[i][0], np.append(data[i][1], has_closed(data[i][1])))
        print(i)
    alphas = kernel(data)
    test_data = get_arrays('test.csv')

    test_data = test_data[0:100]
    #
    for i in range(len(test_data)):
        test_data[i] = (test_data[i][0], np.append(test_data[i][1], has_closed(test_data[i][1])))
        print(i)
    total = 0
    wrong = 0
    for d in test_data:
        answer = decide(d[1], alphas, data)
        if answer != d[0]:

            wrong += 1
            # name = "Images/" + 'wrong_' + str(d[0]) + "_" + str(answer) + '_' + str(total)
            # save_pic(d[1], name)
        else:
            pass
            # name = "Images/" + 'correct_' + str(d[0]) + '_' + str(total)
            # save_pic(d[1], name)
        total += 1
    print('all ' + str(total))
    print("wrong " + str(wrong))



