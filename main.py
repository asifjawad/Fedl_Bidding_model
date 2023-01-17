import numpy as np
import torch
import torchvision
import client as cl



alpha = 0.5
def task():
    """ Contains Job description, that woould be sent to Client, to ask their resources and their Bid"""
    job = {
        "Description" : " Transfer Package",
        "Batter_required" : 30,
           "Time_req": 15,
           } # job description, Battery and time (min)required,

    return job

def Bid_Rule (resource):
    """ Bidding Rule used by client to Perform Resource Value Calculation"""
    rule = resource[0] * alpha + resource[1] * alpha
    return rule


def winner_selection():
    """ Receives bids and calculate No of Winners"""
    pass



if __name__=="__main__":
     print("Biding Process Starting ... !")

     print("Sendiing Bedding Rule to Client")

     print(" Bids received ")

     cl.profit_cal()
