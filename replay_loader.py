import numpy as np
import struct

class ReplaySetter(rlgym_sim.gym.state_setters.StateSetter):
    def reset(self, state_wrapper: rlgym_sim.gym.state_setters.StateWrapper):
        with open("replay.bin", "rb") as f:
            replay_data = f.read()

        current_index = 0

        current_index += 4

        num_frames = struct.unpack_from("<I", replay_data, current_index)[0]
        current_index += 4

        replay_index = np.random.randint(num_frames)
        current_index = replay_index * 36

        ball_position = struct.unpack_from("<2f", replay_data, current_index)
        current_index += 8

        ball_velocity = struct.unpack_from("<2f", replay_data, current_index)
        current_index += 8

        state_wrapper.ball.position = np.array(ball_position, dtype=np.float32)
        state_wrapper.ball.velocity = np.array(ball_velocity, dtype=np.float32)

        for i in range(2):
            car_position = struct.unpack_from("<2f", replay_data, current_index)
            current_index += 8

            state_wrapper.cars[i].position = np.array(car_position, dtype=np.float32)

        for i in range(2):
            car_velocity = struct.unpack_from("<2f", replay_data, current_index)
            current_index += 8

            state_wrapper.cars[i].velocity = np.array(car_velocity, dtype=np.float32)
