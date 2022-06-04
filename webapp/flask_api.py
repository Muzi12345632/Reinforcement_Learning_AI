import gym
import numpy as np
import time

##TODO install mujoco_py module

game= gym.envs.registry
env= gym.make('MountainCar-v0')
NUM_ACTIONS= env.action_space
NUM_STATES= env.observation_space
V= np.zeros_like([NUM_STATES])
Pi= np.zeros_like([NUM_STATES], dtype=float)
rew_total= 0
observation= env.reset()

env.reset()
#env.render()
for _ in range (2000):
    action= env.action_space.sample()
    observation, reward, done, info = env.step(action)
    reward_total= rew_total+ reward
    env.render()


print(NUM_STATES)
print(game)
