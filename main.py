from stakeholder import Node, Aggregator, RoundData

no_of_nodes = 3


def main():
    node = list()
    print("Simulation Started !")
    for id in range(no_of_nodes):
        node_data_list = list()

        if id == 0:
            round1 = RoundData(data=1000, bandwidth=85, p=0.2)
            round2 = RoundData(data=2000, bandwidth=85, p=0.3)

        elif id == 1:
            round1 = RoundData(data=5000, bandwidth=84, p=0.1)
            round2 = RoundData(data=3000, bandwidth=86, p=0.3)

        else:
            round1 = RoundData(data=3000, bandwidth=84, p=0.1)
            round2 = RoundData(data=2000, bandwidth=86, p=0.4)

        node_data_list.append(round1)
        node_data_list.append(round2)

        new_node = Node(str(id), node_data_list)
        node.append(new_node)

    aggregator = Aggregator(node)
    aggregator.RunAggregator()

    print("\n Simulation Finished ! ")


if __name__ == '__main__':
    main()