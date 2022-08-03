import gym
import numpy as np

env= gym.make('FrozenLake8x8-v1')
env.reset()
NUM_ACTIONS= env.action_space.n
NUM_STATES= env.observation_space.n
Q= np.zeros([NUM_STATES, NUM_ACTIONS])

gamma= 0.95
alpha= 0.01 #learning rate
epsilon= 0.5

for episode in range(1, 500001):
    done= False
    observation= env.reset()
    while done != True:
        if np.random.rand(1) < epsilon:
            action= env.action_space.sample()
        else:
            action= np.argmax(Q[observation])

        observation1, reward, done, info= env.step(action)
        Q[observation, action] += alpha *(reward + gamma*np.max(Q[observation1]- Q[observation, action]))
        observation= observation1

    if episode % 5000 == 0:
        reward_average = 0.

        for i in range(100):
            observation= env.reset()
            done= False
            while done != True:
                action = np.argmax(Q[observation])
                observation, reward, done,info= env.step(action)
                reward_average += reward
        env.render()
        reward_average= reward_average/100
        print('Episode {} average reward: {}'.format(episode, reward_average))

        if reward_average > 0.9:
            print('FrozenLake solved')

            break

