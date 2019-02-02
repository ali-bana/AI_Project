import numpy as np
from Opening import *


def len_wid(vector):
    pixels = vector
    pixels = pixels.reshape((28, 28))
    pixels = pixels.tolist()

    up = 0
    found = False
    for row in range(len(pixels)):
        for column in range(len(pixels[row])):
            if pixels[row][column] != 0:
                up = row
                found = True
                break
        if found:
            break

    down = 0
    found = False
    for row in range(len(pixels) -1, -1, -1):
        for column in range(len(pixels[row])):
            if pixels[row][column] != 0:
                down = row
                found = True
                break
        if found:
            break

    left = 0
    found = False
    for column in range(28):
        for row in range(28):
            if pixels[row][column] != 0:
                left = column
                found = True
                break
        if found:
            break

    right = 0
    found = False
    for column in range(27, -1, -1):
        for row in range(28):
            if pixels[row][column] != 0:
                right = column
                found = True
                break
        if found:
            break

    length = right - left
    width = down - up
    return length / width


if __name__ == "__main__":
    pixels = get_arrays('test.csv')
    a = pixels[7][1]
    len_wid(a)
    show_picture(a)