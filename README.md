# Reinforcement_Learning_AI

[![PyPI version](https://badge.fury.io/py/TwitterFollowBot.svg)](https://badge.fury.io/py/TwitterFollowBot)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)

# FrozenLake Problem

The agent controls the movement of a character in a grid world. 
Some tiles of the grid are walkable, and others lead to the agent falling into the water. 
Additionally, the movement direction of the agent is uncertain and only partially depends on the chosen direction. 
The agent is rewarded for finding a walkable path to a goal tile.

# Dependances

Install OpenAI library gym for games using `pip`:
 ```
 
 pip install gym
 pip install tensorflow
 pip install matplotlib
   
 
 ```

# Q-Learning Equation

Q-Learning is a basic form of Reinforcement Learning which uses Q-values (also called action values) to iteratively improve the behavior of the learning agent.

# New Q(s,a) = (1 - learning_rate) x Q(s,a) + learning_rate x [ reward + discount_rate x maxQ(s',a')]
 
 ```
 
 Q[observation, action]  += alpha*(reward+ gamma* np.max(Q[observation2])- Q[observation, action])
 ```

s : Current State of the agent.

a : Current Action Picked according to some policy.

s' : Next State where the agent ends up.

a' : Next best action to be picked using current Q-value estimation, i.e. pick the action with the maximum Q-value in the next state.

R : Current Reward observed from the environment in Response of current action.

𝛾 (>0 and <=1) : Discounting Factor for Future Rewards. Future rewars are less valuable than current rewards so they must be discounted.
Since Q-value is an estimation of expected rewards from a state, discounting rule applies here as well.

𝛼 : Step length taken to update the estimation of Q(S, A).

# Exploration vs Exploitation

Choosing the Action to take using 𝜖 -greedy policy:
```

while done != True:
        if np.random.rand(1) < epsilon:
            action= env.action_space.sample()
        else:
            action= np.argmax(Q[observation])
```

𝜖 -greedy policy of is a very simple policy of choosing actions using the current Q-value estimations. It goes as follows :

With probability (1-  ϵ  ) choose the action which has the highest Q-value.

With probability ( ϵ ) choose any action at random.
<br>
<br>
<br>
Using value iteration approach to exploit the enviroment

```

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
```

