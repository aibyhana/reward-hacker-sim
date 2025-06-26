"# Q-learning agent" 
import numpy as np
import random

class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = [0, 1, 2, 3]
        self.env = env

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        qs = [self.get_q(state, a) for a in self.actions]
        return self.actions[np.argmax(qs)]

    def update(self, state, action, reward, next_state):
        old_q = self.get_q(state, action)
        next_max_q = max([self.get_q(next_state, a) for a in self.actions])
        new_q = old_q + self.alpha * (reward + self.gamma * next_max_q - old_q)
        self.q_table[(state, action)] = new_q
