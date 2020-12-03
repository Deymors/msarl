import numpy as np
import os
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding


# gym.Env parent class: https://github.com/openai/gym/blob/master/gym/core.py


class MSAEnv(gym.Env):

    def __init__(self):
        pass

    # abstract method from parent gym.Env
    def step(self, action):
        pass

    # abstract method from parent gym.Env
    def reset(self):
        pass

    # abstract method from parent gym.Env
    def render(self, mode='human'):
        pass


if __name__ == "__main__":
    env = gym.make("MSAEnv-v0")
