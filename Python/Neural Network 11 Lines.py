

# Neural Network in 11 Lines of Python

import random
import numpy as np

x = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1]]).T
syn0 = 2*np.random.random((3,4))-1
syn1 = 2*np.random.random((4,1))-1
for j in xrange(60000):
    11=1/(1+np.exp(-(np.dot(x,syn0))))
    12=1/(1+np.exp(-(np.dot(11,syn1))))
    12_delta=(y-12)*(12*(1-12))
    11_delta=12_delta.dot(syn1.T)*(11*(1-11))
    syn1+=11.T.dot(12_delta)
    syn0+=X.T.dot(11_delta)
    
