# This module contains modules and classes useful in determining sensor location
# Node - class representing a node, or sensor
# load_known_nodes - loads the known nodes from a csv file

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
        # Go through each line of the file
        for line in file:
            # get each item that is comma-separated
            tokens = line.split(',')
            sensor_list.append(Node(tokens[0], tokens[1]))

        file.close()
    # most likely a file not found error
    except IOError as e:
        print('Error: could not load data from ' + filename)

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

    rssi = {}

    try:
        # make sure the data is in the resources folder
        file = open('res/data/' + filename, 'r')
        # Go through each line of the file
        for line in file:
            # get each item that is comma-separated
            tokens = line.split(',')
            # If the first element isnt a node number, we can skip the line
            try:
                int(tokens[0])
            except ValueError as e:
                continue
            # the first line of the file, we can just append this without doing any formatting
            if tokens[0] == '\n':
                continue
            else:
                # convert the number of walls from strings to floats
                for index, token in enumerate(tokens[1:]):
                    tokens[index + 1] = float(token)
                rssi.append(tokens)

        file.close()
    # most likely a file not found error
    except IOError as e:
        print('Error: could not load data from ' + filename)

    return rssi_matrix

def get_distances(room, unknown_node):
    """
    Calculate the distances from a room to all known nodes based on the rssi values contained within unknown node
    :param room: The room to be examined
    :param node: The unknown node
    :return: A list of distances from room to known nodes
    """
    pass