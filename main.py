# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from scipy.spatial.distance import cdist
import numpy.random as rnd
import time
import numexpr as ne

import cutils
import utils

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# def get_K_matrix(X1,X2, theta):
#     sigma_s2 = theta[0]
#     ls = theta[1:]
#     X1 = X1 @ np.diag(ls)
#     X2 = X2 @ np.diag(ls)
#     d = cdist(X1, X2) ** 2
#     # use fast exp
#     K = sigma_s2 * np.exp(-d)
#     return K

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N = 50000
    x1 = rnd.rand(N, 2)
    x2 = rnd.rand(N, 2)
    l12 = 1
    l22 = 2
    sigma_s2 = 1

    # d_loop = np.zeros((N,N))
    # t0 = time.time()
    # x = x1 @ np.array([[l12, 0], [0, l22]])
    # y = x2 @ np.array([[l12, 0], [0, l22]])
    # for i in range(N):
    #     for j in range(N):
    #         d_loop[i,j] = (x[i,0]-y[j,0])**2 + (x[i,1]-y[j,1])**2
    # K_loop = sigma_s2 * np.exp(-d_loop)
    # t1 = time.time()
    # print('Time for loop: ', t1-t0)


    theta = [sigma_s2, l12, l22]
    t0 = time.time()
    sigma_s2, l12, l22 = theta
    x = x1 @ np.diag([l12, l22])
    y = x2 @ np.diag([l12, l22])
    d_cdist = cdist(x, y) ** 2
    K_cdist = sigma_s2 * np.exp(-d_cdist)
    t1 = time.time()
    print('Time for cdist: ', t1-t0)

    t0 = time.time()
    K = utils.get_K_matrix(x1,x2, [sigma_s2, l12, l22])
    t1 = time.time()
    print('Time for get_K_matrix: ', t1-t0)


    t0 = time.time()
    K = cutils.get_K_matrix(x1,x2, np.array([sigma_s2, l12, l22]).astype(np.double))
    t1 = time.time()
    print('Time for get_K_matrix cython: ', t1-t0)

    exit()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
