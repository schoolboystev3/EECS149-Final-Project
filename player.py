import numpy as np
import math

class Player:
    #location is a length two numpy array
        
    def __init__(self, location = np.array([0,0])):
        self.location = location
        self.points = 0
        self.next_location = np.zeros(2)
        self.order_index = 0
        
    def Move_Player_To_Location(self,new_location):
        self.location = new_location
        
    def Shift_Player(self,shift_distance):
        self.location = np.add(self.location, shift_distance)
        
    def Get_Distance_From_Location(self, location):
        return np.linalg.norm(self.location - location)
    
    def Get_Distance_From_Player(self, adversary):
        return self.Get_Distance_From_Location(adversary.location)
    
    def Add_Point(self):
        self.points += 1
  
    def update_loc(sef, loc):
        self.location = loc

def player_to_adversary_vector(player, adversary):
    return adversary.location - player.location
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
