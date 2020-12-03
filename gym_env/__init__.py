from gym.envs.registration import register

register(
    id='MSAEnv-v0',
    entry_point='gym_env.envs:MSAEnv',
)