import numpy as np
from gym.envs.registration import register

register(
    id='MSAEnv-v0',
    entry_point='gym_env.envs:MSAEnv',
)

register(
    id='MSAEnv-v1',
    entry_point='gym_env.envs:MSAEnv',
    kwargs={'sequences': np.array([
        ['A', 'C', 'G', 'T', 'A'],
        ['C', 'A', 'C', 'G', 'G'],
        ['C', 'G', 'C', 'T', 'A']]
    )}
)

register(
    id='MSAEnv-v2',
    entry_point='gym_env.envs:MSAEnv',
    kwargs={'sequences': np.array([
        ['A', 'G', 'G', 'T', 'A'],
        ['C', 'G', 'C', 'G', 'G'],
        ['C', 'G', 'C', 'T', 'C']]
    )}
)
