
import numpy as np
np.random.seed(42)

# Function that generates a dataset of given number of points in the range x=[low, high]
def generate_set(points, low, high):
    
    X_train = np.random.uniform(low=low,high=high,size=(points))

    std = 0.4
    epsilon = np.random.normal(0,std,size=(points))

    def f(x):
        a_0 = -9.3
        a_1 = 3.5
        return a_0+x*a_1

    y_train = f(X_train)+epsilon+[np.random.normal(0,i) for i in (np.sin(X_train*-10))+1]
    norm_value = np.abs(y_train).max()
    y_train = y_train/norm_value

    return X_train, y_train