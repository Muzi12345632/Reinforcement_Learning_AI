import gym
import numpy as np
import time


env= gym.make('FrozenLake-v1')

Actions = env.action_space.n
States = env.observation_space.n

Q= np.zeros((States, Actions))
Q
Episodes= 20000
Max_steps= 100
Learning_rate= 0.70
Gamma= 0.96

epsilon= 0.9

RENDER= True
rewards= []
for episode in range(Episodes):
    state=env.reset()
    for _ in range(Max_steps):
        if RENDER:
            env.render()

        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        new_state, reward, done, _ = env.step(action)
        Q[state, action] = Q[state, action] + Learning_rate * (reward + Gamma* np.max(Q[new_state,:])- Q[state, action])
        state= new_state

        if done:
            rewards.append(reward)
            episode -= 0.001
            break


print(Q)
print(f'average reward: {sum(rewards)/len(rewards)}:')


#env.reset()
#action= env.action_space.sample()
#observation, reward, done, info = env.step(action)
#print(observation)
#env.render()
#print(observation)
