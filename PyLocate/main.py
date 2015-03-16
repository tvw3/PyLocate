from PyLocate.rooms import *
from PyLocate.sensors import *

r = load_rooms('rooms.csv')
w = load_walls('Walls.csv')
n = load_known_nodes('node_locations.csv')
set_walls(r,w)
r238 = r['R238']
r236 = r['R236']
print(len(r))
for room in r:
    print(r[room].walls)