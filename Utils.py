from collections import namedtuple
from copy import deepcopy
from Opening import *

def find_groups(inpixels):

    width = len(inpixels[0]) + 2
    height = len(inpixels) + 2
    pixels = deepcopy(inpixels)
    for y in pixels:
        y.insert(0, 1)
        y.append(1)
    pixels.insert(0, [1 for x in range(width)])
    pixels.append([1 for x in range(width)])

    queue = [(0,0)]
    visited = [(0,0)]
    while queue:
        y, x = queue.pop(0)

        adjacent = ((y+1, x), (y-1, x), (y, x+1), (y, x-1))
        for n in adjacent:
            if (-1 < n[0] < height and -1 < n[1] < width and
                                        not n in visited and
                                    pixels[n[0]][n[1]] == 1):
                queue.append(n)
                visited.append(n)

    freecoords = [(y-1, x-1) for (y, x) in visited if
                 (0 < y < height-1 and 0 < x < width-1)]
    allcoords = [(y, x) for y in range(height-2) for x in range(width-2)]
    complement = [i for i in allcoords if not i in freecoords]
    bordercoords = [(y, x) for (y, x) in complement if inpixels[y][x] == 0]
    closedcoords = [(y, x) for (y, x) in complement if inpixels[y][x] == 1]

    PixelGroups = namedtuple('PixelGroups', ['free', 'closed', 'border'])
    return PixelGroups(freecoords, closedcoords, bordercoords), closedcoords

def print_groups(ysize, xsize, pixelgroups):
    ys= []
    for y in range(ysize):
        xs = []
        for x in range(xsize):
            if (y, x) in pixelgroups.free:
                xs.append('.')
            elif (y, x) in pixelgroups.closed:
                xs.append('X')
            elif (y, x) in pixelgroups.border:
                xs.append('#')
        ys.append(xs)
    print('\n'.join([' '.join(k) for k in ys]))


def has_closed(vector):
    pixels = vector
    pixels = np.where(pixels > 0.5, 0, 1)
    pixels = pixels.reshape((28, 28))
    pixels = pixels.tolist()
    pixelgroups, closed = find_groups(pixels)
    return len(closed)

if __name__ == "__main__":
   pixels = get_arrays('test.csv')
   pixels = pixels[7][1]
   print(has_closed(pixels))
   pixels = np.where(pixels > 0.5, 0, 1)
   pixels = pixels.reshape((28, 28))
   pixels = pixels.tolist()
   pixelgroups = find_groups(pixels)
   pixelgroups = pixelgroups[0]
   print_groups(28, 28, pixelgroups)
   print("closed: " + str(pixelgroups.closed))