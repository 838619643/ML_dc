import numpy as np
from kmeans import kmeans

def spectral(W, k):
    '''
    SPECTRUAL spectral clustering

        Input:
            W: Adjacency matrix, N-by-N matrix
            k: number of clusters

        Output:
            idx: data point cluster labels, n-by-1 vector.
    '''
    # YOUR CODE HERE
    # begin answer
    D = np.diag(np.sum(W, axis=1))
    L = D - W

    eigval, eigvec = np.linalg.eig(L)
    eigvec_idx = np.argsort(eigval)
    k_eigvec_idx = eigvec_idx[0:k]
    k_eigvec = eigvec[:, k_eigvec_idx]
    
    k_eigvec = np.array(k_eigvec)
    idx = kmeans(k_eigvec, k)
    return idx
    # end answer
