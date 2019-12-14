import file_reader as fr
import time
f_original = open("test_sim_pos.txt", 'w')
f_new = open("new_movement.txt")
f_back_to_original = open("original_movement.txt")
time.sleep(3)
f_original.write(f_new.readline())
time.sleep(4)
f_original = open("test_sim_pos.txt", "w")
f_original.write(f_back_to_original.readline())