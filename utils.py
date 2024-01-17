import numpy as np
from scipy.spatial.distance import cdist

def get_K_matrix(X1,X2, theta):
    sigma_s2 = theta[0]
    ls = theta[1:]
    X1 = X1 @ np.diag(ls)
    X2 = X2 @ np.diag(ls)
    d = cdist(X1, X2) ** 2
    # use fast exp
    K = sigma_s2 * np.exp(-d)
    return K