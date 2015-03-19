# this module contains functions for determining possible room locations
# get_distance - returns the distance given an rssi value and the number of walls


def get_distance(PL, walls):
    """
    gets the distance based on rssi value and the number of walls being measured
    :param PL: The rssi value measured
    :param walls: the number of walls used for determining distance
    :return: the distance in ft
    """
    # reference rssi
    PL0 = -42
    # reference distance in tf
    d0 = 18
    # path loss constant
    alpha = 3
    # wall constant
    k = -9

    return d0 * (10 ** ((PL - PL0 + k * walls)/-(10 * alpha)))


def circle_line_intersection(center, radius, line_start, line_end):
    """
    Determines whether or not a circle and line intersect
    :param center: The center of the circle as a tuple (x,y)
    :param radius: The radius of the circle
    :param line_start: The start point of a line as a tuple (x,y)
    :param line_end: The end point of a line as a tuple (x,y)
    :return: a boolean of whether not the circle intersects the line
    """
    dx = line_end(0) - line_start(0)
    dy = line_end(1) - line_start(1)
    # start calculating the variables for the quadratic used in determining whether or not there is an intersection
    a = dx ** 2 + dy ** 2
    b = 2 * (dx * (line_start(0) - center(0)) + dy * (line_start(1) - center(0)))
    c = (line_start(0) - center(0)) ** 2 + (line_start(1) - center(1)) ** 2 - radius ** 2
    # calculate the determinant to see if there is an intersection
    det = b ** 2 - 4 * a * c
    if det < 0:
        return False
    else:
        return True

def in_range(room, nodes):
    """
    Returns the number of nodes that are in range of a particular room based on rssi value
    :param room: A room object
    :param nodes: A list of all known nodes
    :return: the number of nodes in range of the room
    """


