import numpy as np
import matplotlib.pyplot as plt

""" n = number of points (Resolution), y = predicted value , x = point where x needed, (x0 , y0) = Initial value,
x0,y0 = Initial value to Euler
# x_req = Point where we need to estimate , h = step
"""

x_req = 5
Y0 = 1
x0 = 1
# T = 0.5
no_of_points = [10]

def normalize_data(x):
    norm_res = [(float(i) - min(x)) / (max(x) - min(x)) for i in x]
    return norm_res

def f(y,x):
    return 2*y


def forward_euler(f ,x0, Y0 , x_req  ,n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    y[0] = Y0
    x[0] = x0
    h = (x_req - x[0]) / n
    # print("Step size = ", h)


    # h = T / n

    for k in range(n):
        x[k+1] = x[k] + h
        y[k+1] = y[k] + h * f(y[k], x[k])
    return y, x



def result():
    for n in no_of_points:
        y, x = forward_euler(f , x0=x0, Y0=Y0, x_req = x_req, n=n)
        # print(f"Predicted Value : {y}")
        # print(f"Value of to determine : {x}")
        plt.plot(x,y , linestyle="dashed",label= f" Aprox_n= {n}")


    print(f" At required point {x_req} the predicted value is {y[-1]}")


    plt.plot(x, x*x , label="Orignal function")
    plt.legend()
    plt.show()


# result()
