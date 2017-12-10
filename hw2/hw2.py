import random
import matplotlib.pyplot as plt
import numpy as np

noise_prob=0.8

def sign(x):
    if(x>0):
        return 1;
    return -1;

def error(x,y,s,t):
    err=0
    for i in range(t-1,20):
        if(sign(x[i])!=s):
            err=err+1
    for i in range(0,t-1):
        if(sign(x[i])==s):
            err=err+1
    return err

def train(x,y):
    s=0
    t=0
    err=20
    for ti in range(0,21):
        if(error(x,y,1,ti)<err):
            err=error(x,y,1,ti)
            s=1
            t=ti
        if(error(x,y,-1,ti)<err):
            err=error(x,y,-1,ti)
            s=-1
            t=ti
    return [s,t]
    

random.seed(40)
x = np.zeros(20)
y = np.zeros(20)
array=np.zeros(21)
for a in range(0,1000):
    for i in range(0,20):
        x[i]=random.uniform(-1,1)
        y[i]=sign(x[i])
        noise=random.random()
        if(noise>noise_prob):
            y[i]=y[i]*(-1)
    arg=np.argsort(x)
    x=x[arg]
    y=y[arg]
    result=train(x,y)
    s=result[0]   
    t=result[1]
    array[t]=array[t]+1
for i in range(0,21):
    print(array[i])

