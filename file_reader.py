import numpy as np

def test_format_data(filename):
    data_file = open(filename, "r")
    data = data_file.readline()
    data = data.split() 
    return np.array([float(i) for i in data])

def format_data(filename):
    data_file = open(filename, "r")
    data = data_file.readline()
    data = [float(i) for i in data.split()]
    # format as [player_pos, adv_pos]
    return np.array([data[:2], data[2:4]])
