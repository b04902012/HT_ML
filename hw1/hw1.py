import random
import numpy as np
import matplotlib.pyplot as plt
def sign(n):
    if(n>0):
        return 1
    return -1
data=np.genfromtxt('hw1_8_train.dat')
length=len(data)
data_x=np.append(np.ones((length,1)),data[np.ix_(range(0,length),range(0,4))],axis=1)
data_y=data[np.ix_(range(0,length),[4])]
num_iteration=np.zeros(2000)
for i in range(0,2000):
    random.seed(i)
    random_index=list(range(0,length))
    random.shuffle(random_index)
    random_x=data_x[random_index]
    random_y=data_y[random_index]
    error=True
    w=np.zeros(5)
    init_index=0
    while(error):
        error=False
        for j in range(0,length):
            idx=(j+init_index)%length
            if(sign(np.inner(w,random_x[idx]))!=random_y[idx]):
                error=True
                w=w+0.5*random_y[idx]*random_x[idx]
                init_index=(idx+1)%length
                break
        if(error==False):
            break
        num_iteration[i]=num_iteration[i]+1
plt.hist(num_iteration,bins='auto')
plt.axvline(num_iteration.mean(), color='r', linestyle='dashed', linewidth=2)
plt.savefig('histogram.png')
print(np.mean(num_iteration))
