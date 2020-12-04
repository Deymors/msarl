import numpy as np
import os
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding


# gym.Env parent class: https://github.com/openai/gym/blob/master/gym/core.py
from gym_env.envs.MsaAction import MsaAction


class MSAEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, sequences):
        '''
        :param sequences: nucleic acid sequence
        :type sequences: numpy.array
        '''
        self.state = sequences  # passed as kwargs in msarl/gym_env/__init__.py register calls
        num_rows, num_cols = sequences.shape
        self.action_space = [(i // num_rows, i % num_cols) for i in range(num_rows * num_cols)] # coordinate at which we add a gap
        self.observation_space = None  #TODO

    # abstract method from parent gym.Env
    def step(self, action: MsaAction):
        pass

    # abstract method from parent gym.Env
    def reset(self):
        pass

    # abstract method from parent gym.Env
    def render(self, mode='human'):  # third option: close=False
        pass
