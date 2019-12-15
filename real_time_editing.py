import file_reader as fr
import time
time.sleep(14)
f_original = open("test_sim_pos.txt", 'w')
f_new = open("new_movement.txt")
f_back_to_original = open("original_movement.txt")
f_original.write(f_new.readline())
f_original.close()
time.sleep(5)
f_original = open("test_sim_pos.txt", "w")
f_original.write(f_back_to_original.readline())
f_original.close()
