import numpy as np
import math

pixel_to_distance = 0.2
close_limit = 0.00001

class Player:
    #location is a length two numpy array
        
    def __init__(self, location = np.array([0,0])):
        self.location = location
        self.score = 0
        self.next_location = np.zeros(2)
        self.order_index = 0
        self.rally_points = np.zeros(1)
        
    def Move_Player_To_Location(self,new_location):
        self.location = new_location
        
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

def player_to_adversary_vector(player, adversary):
    direction = adversary.location - player.location
    ret = direction * pixel_to_distance / np.linalg.norm(direction)
    if (np.linalg.norm(ret) < close_limit):
        return np.zeros(2)
    return ret


def go_to_random_rally_point(player):
    print(player.next_location)
    if(not player.next_location.all()):
        player.next_location = player.rally_points[np.random.randint(0, len(player.rally_points))]

        
    
    near_point = player.Get_Distance_From_Location(player.next_location) < 0.3
    if not near_point:
        direction = player.next_location - player.location
        direction = direction
        return direction
    else:
        player.next_location = np.zeros(2)
        return player.next_location

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
