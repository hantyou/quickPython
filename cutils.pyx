# filename: my_module.pyx
import numpy as np
cimport numpy as np
from scipy.spatial.distance import cdist

cpdef np.ndarray[double, ndim=2] get_K_matrix(np.ndarray[double, ndim=2] X1, np.ndarray[double, ndim=2] X2, np.ndarray[double, ndim=1] theta):
    cdef double sigma_s2 = theta[0]
    cdef np.ndarray[double, ndim=1] ls = theta[1:]
    X1 = X1 @ np.diag(ls)
    X2 = X2 @ np.diag(ls)
    cdef np.ndarray[double, ndim=2] d = cdist(X1, X2) ** 2
    # use fast exp
    cdef np.ndarray[double, ndim=2] K = sigma_s2 * np.exp(-d)
    return K