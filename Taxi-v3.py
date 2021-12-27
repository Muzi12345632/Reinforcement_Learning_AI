import gym
import numpy as np
from gym import envs



#### VALUE ITERATION ALGORITHM


env = gym.make('Taxi-v3')
NUM_ACTIONS= env.action_space.n
NUM_STATES= env.observation_space.n
V= np.zeros([NUM_STATES])
Pi= np.zeros([NUM_STATES], dtype=int)

rew_total= 0
observation= env.reset()
#observation= env.reset()
#done= False
env.render()
#for _ in range (6):
    #action= env.action_space.sample()
    #observation, reward, done, info = env.step(action)
    #reward_total= rew_total+ reward
    #env.render()


gamma= 0.9
significant_improvement= 0.01

#find highest value action in state s
def best_action_value(s):
    best_a= None
    best_value= float('-inf')

    for a in range(0, NUM_ACTIONS):
        env.env.s= s
        new_s, rew, done, info= env.step(a)
        v= rew + gamma*V[new_s]
        if v > best_value:
            best_value= v
            best_a= a
    return best_a

iteration = 0

while True:
    biggest_change= 0
    for s in range (0, NUM_STATES):
        old_v= V[s]
        action= best_action_value(s)
        env.env.s= s
        new_s, rew, done, info= env.step(action)
        V[s]= rew + gamma*V[new_s]
        Pi[s]= action
        biggest_change= max(biggest_change, np.abs(old_v- V[s]))
        iteration += 1

        if biggest_change < significant_improvement:
            #print(iteration, 'iterations were done')
            break


    rew_total= 0
    env.render()
    observation= env.reset()
    done= False

    while done != True:
        action = Pi[observation]
        observation,  rew, done, info= env.step(action)
        rew_total = rew_total + rew
        env.render()

    print("reward: %r"% rew_total)




