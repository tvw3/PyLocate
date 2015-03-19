# This module contains modules and classes useful in determining sensor location
# Node - class representing a node, or sensor
# load_known_nodes - loads the known nodes from a csv file
# load_rssi - loads the rssi value into a matrix
# set_rssi - sets the rssi value of each node so that every node has access to the rssi value of its links with other
#   nodes


import sys


class Node():
    """
    Representation of a sensor in the network
    """
    def __init__(self, number, room):
        """
        Inits a node
        :param number: the node id number
        :param room: the room in which to the node is located. Should be an empty string if the room is unknown or not
        yet assigned
        :return:
        """
        self.id = number
        self.room = room
        # Rssi values between this node and other nodes
        self.links = {}


def load_known_nodes(filename):
    """
    Loads all known node room locations from a csv
    :param filename: the name of the csv file
    :return: a list of nodes
    """
    name, ext = filename.split('.')
    if ext != 'csv':
        # Not a csv, update the user and shut down the program
        print('Error: Cannot load ' + filename + '. File type must be csv')
        sys.exit(-1)

    sensor_list = []

    try:
        # make sure the data is in the resources folder
        file = open('res/data/' + filename, 'r')
    # most likely a file not found error
    except IOError as e:
        print('Error: could not load data from ' + filename)
    else:
        # Go through each line of the file
        for line in file:
            # get each item that is comma-separated
            tokens = line.split(',')
            if '\n' in tokens[1]:
                tokens[1] = tokens[1].replace('\n', '')
            sensor_list.append(Node(tokens[0], tokens[1]))
        file.close()

    return sensor_list


def load_rssi(filename):
    """
    Loads the rssi data from a csv file
    :param filename: the csv file to load from
    :return: nested list containing the rssi values
    """
    # separate the filename and extension to verify that we are working with a csv file
    name, ext = filename.split('.')
    if ext != 'csv':
        # Not a csv, update the user and shut down the program
        print('Error: Cannot load ' + filename + '. File type must be csv')
        sys.exit(-1)

    rssi = []
    sending = []
    receiving = []
    value = []

    try:
        # make sure the data is in the resources folder
        file = open('res/data/' + filename, 'r')
    # most likely a file not found error
    except IOError as e:
        print('Error: could not load data from ' + filename)
    else:
        # Go through each line of the file
        for line in file:
            # get each item that is comma-separated
            tokens = line.split(',')
            # If the first element isnt a node number, we can skip the line
            try:
                int(tokens[0])
            except ValueError as e:
                continue
            else:
                # to handle weird cases where a line contains only a newline
                if tokens[0] == '\n':
                    continue
                else:
                    sending.append(int(tokens[0]))
                    receiving.append(int(tokens[1]))
                    value.append(float(tokens[2]))

        # Create the matrix for sending and receiving nodes
        rssi = [[[] for row in range(max(sending) + 1)] for col in range(max(receiving) + 1)]
        # compile the 3 lists into the matrix
        for i in range(len(sending)):
            rssi[sending[i]][receiving[i]] = value[i]
        # each element in the matrix is a list of all rssi values - average each list to get a single number for each
        # element
        for i in range(len(rssi)):
            for j in range(len(rssi[i])):
                try:
                    rssi[i][j] = sum(rssi[i][j]) / len(rssi[i][j])
                # Bad juju here, but I'm feeling lazy. Possible errors are divide by zero and type error for a single
                # value instead of a list
                except Exception as e:
                    pass

        file.close()
    return rssi


def set_rssi(nodes, rssi):
    """
    Sets each nodes rssi links to other nodes
    :param nodes: A list of nodes
    :param rssi: a table of rssi values between nodes
    :return: an updated list of nodes
    """
    for i, node in enumerate(nodes):
        data = rssi[int(node.id)]
        for j, value in enumerate(data):
            nodes[i].links[str(j)] = value

    return nodes
