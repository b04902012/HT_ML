import random
import matplotlib.pyplot as plt
import numpy as np

noise_prob=0.8

def sign(x):
    if(x>0):
        return 1;
    return -1;

def error_in(x,y,s,t):
    err=0
    for i in range(t-1,20):
        if(y[i]!=s):
            err=err+1
    for i in range(0,t-1):
        if(y[i]==s):
            err=err+1
    return err/20

def error_out(x,y,s,t):
    theta=0
    if(t==0):
        theta=(-1+x[0])/2
    elif(t==20):
        theta=(x[19]+1)/2
    else:
        theta=(x[t-1]+x[t])/2
    return 0.5+0.3*s*(theta*sign(theta)-1)

def train(x,y):
    s=0
    t=0
    err=20
    for ti in range(0,21):
        if(error_in(x,y,1,ti)<err):
            err=error_in(x,y,1,ti)
            s=1
            t=ti
        if(error_in(x,y,-1,ti)<err):
            err=error_in(x,y,-1,ti)
            s=-1
            t=ti

    return [s,t]
    

random.seed(0)
x = np.zeros(20)
y = np.zeros(20)
array=np.zeros(21)
e_in=np.zeros(1000)
e_out=np.zeros(1000)
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
    e_in[a]=error_in(x,y,s,t)
    e_out[a]=error_out(x,y,s,t)

colors=np.random.rand(1000)
plt.scatter(e_out,e_in,c=colors,alpha=0.3)
plt.savefig('err.png')
plt.show()
