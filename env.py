"# Toy environment with reward function" 
import numpy as np
import numpy as np

class GridWorld:
    def __init__(self, hack_enabled=True):
        self.size = 5
        self.goal = (4, 4)
        self.hack_tile = (2, 2)
        self.hack_enabled = hack_enabled
        self.reset()

    def reset(self):
        self.agent_pos = [0, 0]
        return tuple(self.agent_pos)

    def step(self, action):
        if action == 0:  # up
            self.agent_pos[0] = max(self.agent_pos[0] - 1, 0)
        elif action == 1:  # down
            self.agent_pos[0] = min(self.agent_pos[0] + 1, self.size - 1)
        elif action == 2:  # left
            self.agent_pos[1] = max(self.agent_pos[1] - 1, 0)
        elif action == 3:  # right
            self.agent_pos[1] = min(self.agent_pos[1] + 1, self.size - 1)

        pos = tuple(self.agent_pos)
        reward = 0
        done = False

        if pos == self.goal:
            reward = 1
            done = True
        elif self.hack_enabled and pos == self.hack_tile:
            reward = 100  # intentional hack

        return pos, reward, done


