REWARD = 0.0

TERMINAL = [
    rlgym_sim.gym.terminal_conditions.GoalScoredCondition(),
    rlgym_sim.gym.terminal_conditions.TimeoutCondition(45)
]

class Obs(rlgym_sim.gym.obs_builder.ObsBuilder):
    def reset(self, initial_state: rlgym_sim.gym.GameState):
        pass

    def build_obs(self, player: rlgym_sim.gym.PlayerData, state: rlgym_sim.gym.GameState, previous_action: np.ndarray) -> np.ndarray:
        obs = [
            player.car_data.position[0],
            player.car_data.position[1],
            player.car_data.velocity[0],
            player.car_data.velocity[1],
            state.ball.position[0],
            state.ball.position[1],
            state.ball.linear_velocity[0],
            state.ball.linear_velocity[1],
        ]

        return np.array(obs, dtype=np.float32)
