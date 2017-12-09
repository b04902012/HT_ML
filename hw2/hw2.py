import random
import matplotlib.pyplot as plt
import numpy as np

noise_prob=0.8

def sign(x):
    if(x>0):
        return 1;
    return -1;

random.seed(0)
x = np.zeros(20)
y = np.zeros(20)
for i in range(0,20):
    x[i]=random.uniform(-1,1)
    y[i]=sign(x[i])
    noise=random.random()
    if(noise>noise_prob):
        y[i]=-y[i]
    
