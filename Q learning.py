import gym
import numpy as np
import time


#### Q-LEARNING ALGORITHM


env= gym.make('Taxi-v3')
NUM_ACTIONS=  env.action_space.n
NUM_STATES= env.observation_space.n
Q= np.zeros([NUM_STATES, NUM_ACTIONS])

gamma= 0.9
alpha=0.9 #learning rate

for episode in range(1, 1001):
    done= False
    reward_total=0
    observation= env.reset()
    while done != True:
        action= np.argmax(Q[observation]) # choosing action with highest Q value
        observation2, reward, done, info= env.step(action)
        Q[observation, action]  += alpha*(reward+ gamma* np.max(Q[observation2])- Q[observation, action])
        reward_total= reward_total + reward
        observation= observation2

    if episode % 50 == 0:
        print('Episode {} Total Reward: {}'.format(episode, reward_total))

########using policy to take action delivering max value

rew_total=0
obs= env.reset()
env.render()
done= False
while done != True:
    action= np.argmax(Q[obs])
    obs, rew, done,info= env.step(action)
    rew_total= rew_total + rew
    env.render()
print("Reward : %r" % rew_total)



