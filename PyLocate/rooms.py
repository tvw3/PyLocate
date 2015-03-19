# this module is used to model and manage rooms in a building
# Room - room class used to store data relating to the room, as well as provide additional information that connects
#       this room to other rooms, such as the number of walls
# load_rooms - functions that loads in room data from a csv file and returns a list of Room objects

import sys

# The scale from measurements of rooms on paper to real-life measurements
scale = 12.5


class Room():
    """
    room class used to store data relating to the room, as well as provide additional information that connects
    this room to other rooms, such as the number of walls
    """
    def __init__(self, room_name, x, y, width, height):
        """
        Constructor
        :param: room_name: the name of the room
        :param x: the x location of the room as it relates to the floormap
        :param y: the y location of the room as it relates to the floormap
        :param width:  the width of the room
        :param height: the hight of the room
        :return:
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room_name = room_name
        # dictionary whose key is the name of another room and value is the number of walls between the two rooms
        self.walls = {}

    def get_center(self):
        """
        returns the center of the room
        :return: a tuple (x,y)
        """
        # Rooms measured to the top left corner, so we add width, and subtract height to get midpoints
        c_x = (self.x + (self.x + self.width)) / 2
        c_y = (self.y + (self.y - self.height)) / 2
        return c_x, c_y

    def get_walls_between(self, other_room):
        """
        returns the number of walls between this room and other_room
        :param: other_room: A room object
        :return: the number of walls between the 2 rooms
        """
        return self.walls[other_room.room_name]


def load_rooms(filename):
    """
    Loads the room data from the csv stored in file name
    :param filename:
    :return: a dictionary containing all rooms
    """
    # return dictionary containing all the rooms
    room_list = {}
    # separate the filename and extension to verify that we are working with a csv file
    name, ext = filename.split('.')
    if ext != 'csv':
        # Not a csv, update the user and shut down the program
        print('Error: Cannot load ' + filename + '. File type must be csv')
        sys.exit(-1)

    try:
        # make sure the data is in the resources folder
        file = open('res/data/' + filename, 'r')
        # Go through each line of the file
        for line in file:
            # get each item that is comma-separated
            tokens = line.split(',')
            # the first line of the file, we don't want to do anything here
            if tokens[0] == 'name':
                continue
            elif tokens[0] == '\n':
                continue
            else:
                room_list[tokens[0]] = Room(
                    tokens[0],
                    float(tokens[1]) * scale,
                    float(tokens[2]) * scale,
                    float(tokens[3]) * scale,
                    float(tokens[4]) * scale
                )

        file.close()
    # most likely a file not found error
    except IOError as e:
        print('Error: could not load data from ' + filename)

    return room_list


def load_walls(filename):
    """
    Loads the wall data from the csv stored in file name
    :param filename:
    :return: a nested list containing the number of walls between each room
    """
    # return list
    wall_matrix = []
    # separate the filename and extension to verify that we are working with a csv file
    name, ext = filename.split('.')
    if ext != 'csv':
        # Not a csv, update the user and shut down the program
        print('Error: Cannot load ' + filename + '. File type must be csv')
        sys.exit(-1)

    try:
        # make sure the data is in the resources folder
        file = open('res/data/' + filename, 'r')
        # Go through each line of the file
        for line in file:
            # get each item that is comma-separated

            tokens = line.split(',')
            # the first line of the file, we can just append this without doing any formatting
            if tokens[0] == '':
                #remove the last new line characters from room names
                if '\n' in tokens[len(tokens) - 1]:
                    tokens[len(tokens) - 1] = tokens[len(tokens) - 1].replace('\n', '')
                wall_matrix.append(tokens)
            elif tokens[0] == '\n':
                continue
            else:
                # convert the number of walls from strings to floats
                for index, token in enumerate(tokens[1:]):
                    tokens[index + 1] = float(token)
                wall_matrix.append(tokens)

        file.close()
    # most likely a file not found error
    except IOError as e:
        print('Error: could not load data from ' + filename)

    return wall_matrix


def set_walls(rooms, walls):
    """
    Sets the number of walls between every room
    :param rooms: Dictionary of room objects
    :param walls: nested list containing number of walls between each room
    :return: the updated rooms dictionary
    """
    # loop through all walls except the first row, since does not contain any values, only room names
    for wall_set in walls[1:]:
        # for each wall in the set (exclude the first element, because that is the room name)
        for index, wall in enumerate(wall_set[1:]):
            # use the room name (first element of wall set) as a key to find the room to add walls to
            # then use other room associated with the number of walls (the first row of the walls parameter passed in)
            # as a key for the walls dictionary in each room object. Assign the value for that key to wall
            rooms[wall_set[0]].walls[walls[0][index + 1]] = wall

    return rooms





