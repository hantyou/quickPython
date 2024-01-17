# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from scipy.spatial.distance import cdist
import numpy.random as rnd
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N = 10000
    x1 = rnd.rand(N, 2)
    x2 = rnd.rand(N, 2)

    d_loop = np.zeros((N,N))
    t0 = time.time()
    for i in range(N):
        for j in range(N):
            d_loop[i,j] = np.sqrt((x1[i,0]-x2[j,0])**2 + (x1[i,1]-x2[j,1])**2)
    t1 = time.time()
    print('Time for loop: ', t1-t0)

    t0 = time.time()
    d_cdist = cdist(x1, x2)
    t1 = time.time()
    print('Time for cdist: ', t1-t0)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
