import numpy as np
from dataclasses import dataclass

K = 3

BANDWIDTH_MIN = 5
BANDWIDTH_MAX = 100

DATA_MIN = 1000
DATA_MAX = 5000

P_MIN = 0.021334328158479184
P_MAX = 0.03875953108451435

ALPHA_DATA = 0.5
ALPHA_BANDWIDTH = 0.5
alpha = np.array([ALPHA_DATA, ALPHA_BANDWIDTH])

COST_DATA = 0.4
COST_BANDWIDTH = 0.6

cost = np.array([COST_DATA, COST_BANDWIDTH])


@dataclass
class RoundData():
    data: int
    bandwidth: int
    p: float

    def __init__(self, data: int, bandwidth: int, p: float):
        self.data = data
        self.bandwidth = bandwidth
        self.p = p


""" Function withou classes """


def normalize(data, data_min, data_max):
    d = (data - data_min) / (data_max - data_min)
    return d


def scoring_function(q, p):
    return np.min(alpha * q) + p


def calculate_p(q):
    resource_value = sum(alpha * q)
    resource_cost = sum(cost * q)
    profit = resource_value - resource_cost

    euler = Euler()
    p = euler.approximate_value(profit)

    # p = forward_euler(profit)

    return round(p, 2)


""" Functions"""


class Euler():
    def __init__(self, X_init=1, Y_init=1, step=10):
        self.x = np.zeros(step + 1)
        self.y = np.zeros(step + 1)

        self.x[0] = X_init
        self.y[0] = Y_init
        self.step = step

    def function(self, y, x):
        return y

    def approximate_value(self, x_required):
        h = (x_required - self.x[0]) / self.step

        for k in range(self.step):
            self.x[k + 1] = self.x[k] + h
            self.y[k + 1] = self.y[k] + h * self.function(self.y[k], self.x[k])
        return self.y[-1]


class Node():
    def __init__(self, id, node_data_list):
        self.id = id
        self.node_data_list = node_data_list

    def collect_data(self, round):
        q = np.array([normalize(self.node_data_list[round].data, DATA_MIN, DATA_MAX),
                      normalize(self.node_data_list[round].bandwidth, BANDWIDTH_MIN, BANDWIDTH_MAX)])
        # Calulate value of p
        p = calculate_p(q)

        # p = self.node_data_list[round].p
        return (q, p)


class Aggregator():
    def __init__(self, nodes, num_of_rounds=2):
        self.nodes = nodes
        self.num_of_rounds = num_of_rounds

        self.board = list()
        board1 = list()
        board2 = list()

        self.board.append(board1)
        self.board.append(board2)

    def RunAggregator(self):

        for round in range(self.num_of_rounds):
            print("\n[Aggregator]: Round " + str(round))

            for node in self.nodes:
                data = node.collect_data(round)
                # print(data)

                bid = scoring_function(data[0], data[1])
                # bid = round(bid,4)

                print("[Aggregator]: Score Received " + str(bid) + " from node " + str(node.id))

                self.board[round].append((node.id, bid, data[1]))

            self.board[round].sort(key=lambda x: x[1])

            top_k = self.board[round][-K:]
            for k in top_k:
                print("[Aggregator]: Round [" + str(round) + "] Winner node " + str(k[0]) + " score [" + str(
                    k[1]) + "] and P [" + str(k[2]) + "]")


