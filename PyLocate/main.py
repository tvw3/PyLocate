from PyLocate.rooms import *
from PyLocate.sensors import *
from PyLocate.localize import *
from math import sqrt

r = load_rooms('rooms.csv')
w = load_walls('Walls.csv')
n = load_known_nodes('node_locations.csv')
set_walls(r,w)
rssi = load_rssi('rssi_data_trial_1.csv')
set_rssi(n, rssi)
print(n[6].id)
print(n[6].room)
print(n[6].links['5'])
print(r['R234'].walls[n[6].room])
print(get_distance(n[6].links['6'], r['R234'].walls[n[6].room]))
print('Actual distance')
end = r['R236A']
end = end.get_center()
start = r['R234']
start = start.get_center()
x_dif = end[0] - start[0]
y_dif = end[1] - start[1]
print(sqrt(x_dif ** 2 + y_dif ** 2))


