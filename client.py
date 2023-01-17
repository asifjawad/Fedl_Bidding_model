import numpy as np
import torch
import torchvision

import main
import functions as fun
import random

"""Minimum point for resource [10, 5] for battery and availability
 - profit is 3.5 so we can set this as starting point for Euler
 so x0 = 3.5 , y0 = 1
 """

x0 = 3.5
Y0 = 1
alpha = 0.5


resource_1 = random.randint(10,100) # we can set a range for battery/resources

resource = [20, 10]


def calculate_Profit(alpha, resource):
    scoring_res = sum([i * alpha for i in resource])

    cost_res = sum([0.3*resource[0], 0.2*resource[1]])         # each resoruce cost per_unit.

    profit = scoring_res - cost_res

    return profit , scoring_res , cost_res



def task_rec():

    job = main.task()
    li= [i for i in job.values()]
    print(li)
    print("Bid request is Received")
    alpha = 0.5
    rul = main.bid_rule(resource)
    print(rul)



def f(y,x):
    return y

def profit_cal():

    profit, scoring_res, cost_res = calculate_Profit(alpha, resource)
    print(f"Profit Calculated is = {profit}",)
    print(f"Resource Score = {scoring_res}",)
    print(f"Resource Cost = {cost_res}",)

    for n in [20]:
        y, x = fun.forward_euler(f,x0 = x0 ,Y0 = Y0,x_req = profit,n = n)

    print(f" The Profit of Client [1] =  {profit} , the bidding value =  {y[-1]}")



