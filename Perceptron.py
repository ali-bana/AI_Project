import numpy as np
import math
from Opening import get_arrays
from Opening import show_picture

def perceptron(data, number):
    weights = []
    # print(data[0][1])
    for i in range(0, 10):
        weights.append(np.array([0.0 for _ in range(data[0][1].size)], dtype='float'))

    i = 0
    # for w in weights:
    #     print(w)
    for d in data:
        answer = decide(d[1], weights)
        if i == number:
            break
        if answer != d[0]:
            theta = min(cal_tetha(d[1], weights[d[0]], weights[answer]), 0.003)
            # theta = 0.0028 #this is the best for 60000
            theta = 1
            weights[answer] -= theta * d[1]
            weights[d[0]] += theta * d[1]
            # weights[d[0]] = normalize(weights[d[0]])
            # weights[answer] = normalize(weights[answer])
            i += 1
        i += 1
    print(i)
    return weights

def cal_tetha(f, correct, wrong):
    theta = np.dot((wrong - correct), f) + 1
    return theta /( 2 * np.dot(f, f))

def normalize(arr):
    return (1 / math.sqrt(np.dot(arr, arr))) * arr


def decide(data, weights):
    products = []
    for i in range(0, len(weights)):
        products.append(np.dot(data, weights[i]))
    result = 0
    for i in range(0, len(products)):
        if products[i] > products[result]:
            result = i
    return int(result)

if __name__ == "__main__":
    theta = [60000]
    data = get_arrays('data.csv')
    test = get_arrays('test.csv')
    for t in theta:
        weights = perceptron(data, t)
        all = 0
        wrong = 0
        for d in test:
            all += 1
            answer = decide(d[1], weights)
            if answer != d[0]:
                #show_picture(d[1])
                wrong += 1
        print('all ' + str(all))
        print('wrong ' + str(wrong))
        print((all-wrong) / all)