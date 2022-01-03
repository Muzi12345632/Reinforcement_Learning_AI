# Reinforcement_Learning_AI
Reinforcement AI

# FrozenLake Problem

The agent controls the movement of a character in a grid world. 
Some tiles of the grid are walkable, and others lead to the agent falling into the water. 
Additionally, the movement direction of the agent is uncertain and only partially depends on the chosen direction. 
The agent is rewarded for finding a walkable path to a goal tile.


# Q-Learning Equation

Q-Learning is a basic form of Reinforcement Learning which uses Q-values (also called action values) to iteratively improve the behavior of the learning agent.

# New Q(s,a) = (1 - learning_rate) x Q(s,a) + learning_rate x [ reward + discount_rate x maxQ(s',a')]
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

𝜖 -greedy policy of is a very simple policy of choosing actions using the current Q-value estimations. It goes as follows :

With probability (1-  ϵ  ) choose the action which has the highest Q-value.

With probability ( ϵ ) choose any action at random.
