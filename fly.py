import time

import cflib.crtp
import file_reader as fr
import player as pl
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger

# URI to the Crazyflie to connect to
uri = 'radio://0/80/2M'

HEIGHT = 0.5
YAW = 0.0

def wait_for_position_estimator(scf):
    print('Waiting for estimator to find position...')

    log_config = LogConfig(name='Kalman Variance', period_in_ms=500)
    log_config.add_variable('kalman.varPX', 'float')
    log_config.add_variable('kalman.varPY', 'float')
    log_config.add_variable('kalman.varPZ', 'float')

    var_y_history = [1000] * 10
    var_x_history = [1000] * 10
    var_z_history = [1000] * 10

    threshold = 0.001

    with SyncLogger(scf, log_config) as logger:
        for log_entry in logger:
            data = log_entry[1]

            var_x_history.append(data['kalman.varPX'])
            var_x_history.pop(0)
            var_y_history.append(data['kalman.varPY'])
            var_y_history.pop(0)
            var_z_history.append(data['kalman.varPZ'])
            var_z_history.pop(0)

            min_x = min(var_x_history)
            max_x = max(var_x_history)
            min_y = min(var_y_history)
            max_y = max(var_y_history)
            min_z = min(var_z_history)
            max_z = max(var_z_history)

            # print("{} {} {}".
            #       format(max_x - min_x, max_y - min_y, max_z - min_z))

            if (max_x - min_x) < threshold and (
                    max_y - min_y) < threshold and (
                    max_z - min_z) < threshold:
                break


def reset_estimator(cf):
    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')

    wait_for_position_estimator(cf)


def activate_high_level_commander(cf):
    cf.param.set_value('commander.enHighLevel', '1')

def test_movement(cmdr):
    relative = True
    data = fr.test_format_data("test_movement.txt")
    cmdr.go_to(data[0], data[1], 0.0, YAW, 1.0, relative) 

def update_movement(cmdr, player, adversary):
    relative = True
    data = fr.format_data("test_sim_pos.txt")
    player.update_loc(data[0])
    adversary.update_loc(data[1])
    x, y = pl.player_to_adversary_vector(player, adversary)
    cmdr.go_to(x, y, 0.0, YAW, 1.0, relative) 

if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf

        activate_high_level_commander(cf)
        reset_estimator(cf)
        
        cmdr = cf.high_level_commander
        # player = pl.Player()
        # adversary = pl.Player()
 
        cmdr.takeoff(HEIGHT, 2.0)
        time.sleep(3.0)
        
        """
        # simulate square movement

        count = 0
        f0 = open("test_sequence_sim.txt")
        f1 = open("test_sim_pos", "w")
        
        while count < 4:
            f1.write(f0.readline())
            update_movement(cmdr, player, adversary)
            count += 1
            time.sleep(1.0)
        """
      
        # update_movement(cmdr, player, adversary)
        # time.sleep(3.0)

        test_movement(cmdr)
        time.sleep(2.0)
        
        cmdr.land(0.0, 2.0)
        time.sleep(2.0)
        
        cmdr.stop()
