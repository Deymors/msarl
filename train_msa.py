import gym
import gym_env  # name from setup.py
import numpy as np


env = gym.make('MSAEnv-v2')  # requires import gym_env
print(env.action_space)

