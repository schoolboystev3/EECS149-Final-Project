import numpy as np
import math

pixel_to_distance = 0.2
close_limit = 0.0001
# moving is limited to pixel_to_distance length movements so the closest the drone will ever be to
# a destination is half that movement distance
close = pixel_to_distance / 2

class Player:
    #location is a length two numpy array
        
    def __init__(self, location = np.array([0,0])):
        self.location = location
        self.score = 0
        self.next_location = np.array([])
        self.order_index = 0
        self.rally_points = np.zeros(1)
         
    def Shift_Player(self,shift_distance):
        self.location = np.add(self.location, shift_distance)
        
    def Get_Distance_From_Location(self, location):
        return np.linalg.norm(self.location - location)
    
    def Get_Distance_From_Player(self, adversary):
        return self.Get_Distance_From_Location(adversary.location)
    
    def Add_Point(self):
        self.score += 1
  
    def update_loc(self, loc):
        self.location = loc

    def set_rally_points(self, rally_points):
        self.rally_points = rally_points

def get_dist_to_dest(player):
    return player.Get_Distance_From_Location(player.next_location)

def move_player(start, dest):
    direction = dest - start
    ret = direction * pixel_to_distance / np.linalg.norm(direction)
    if (np.linalg.norm(ret) < close):
        return np.zeros(2)
    return ret

def player_to_adversary_vector(player, adversary):
    return move_player(player.location, adversary.location)

def go_to_random_rally_point(player):
    # intialize next random location
    if(player.next_location.size == 0):
        player.next_location = player.rally_points[np.random.randint(0, len(player.rally_points))]
    
    near_point = player.Get_Distance_From_Location(player.next_location) <= close
    
    if(near_point):
        player.next_location = player.rally_points[np.random.randint(0, len(player.rally_points))]
     
    print(player.next_location)
    
    return move_player(player.location, player.next_location)

"""
yaw = 0
height = 0.5

vector = np.zeros(4)
vector[2] = yaw
vector[3] = height

def loop(player, adversary, func):
    count = 0
    while count < 10:
        count += 1
        # set the player locations using player.Get_Distance_From_Location()
        vector[0], vector[1] = player_to_adversary_vector(player, adversary)
        func(vector[0], vector[1], vector[2], vector[3])
        time.sleep(1)
        
player = Player()
adversary = Player()
loop(player, adversary)
"""
