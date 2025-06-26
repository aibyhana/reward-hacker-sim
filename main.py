# main.py — Entry point with reward hack detection and heatmap generation

from env import GridWorld
from agent import QLearningAgent
from detector import detect_reward_hacking
from plot_utils import plot_rewards
import numpy as np
import matplotlib.pyplot as plt

NUM_EPISODES = 200
MAX_STEPS = 100  # prevent infinite loops

# ---------- First Run: No Reward Hack ----------
print("\n===== PHASE 1: Training without reward hack =====")

env = GridWorld(hack_enabled=False)
agent = QLearningAgent(env)
rewards_no_hack = []
visits_no_hack = np.zeros((env.size, env.size))

for episode in range(NUM_EPISODES):
    total_reward = 0
    state = env.reset()
    done = False
    steps = 0

    while not done and steps < MAX_STEPS:
        action = agent.select_action(state)
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state)
        state = next_state
        total_reward += reward
        steps += 1
        visits_no_hack[state[0], state[1]] += 1

    rewards_no_hack.append(total_reward)

# Plot and save reward curve (no hack)
plt.figure()
plot_rewards(rewards_no_hack, title='Reward per Episode (No Hack)')
plt.savefig('reward_no_hack.png')
print('✅ Saved: reward_no_hack.png')

# Plot and save heatmap (no hack)
plt.figure()
plt.imshow(visits_no_hack, cmap='hot', interpolation='nearest')
plt.title('Tile Visit Heatmap (No Hack)')
plt.colorbar(label='Visit Frequency')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.savefig('heatmap_no_hack.png')
print('✅ Saved: heatmap_no_hack.png')

# ---------- Second Run: With Reward Hack Enabled ----------
print("\n===== PHASE 2: Training with reward hack enabled =====")

env = GridWorld(hack_enabled=True)
agent = QLearningAgent(env)
rewards_hack = []
visits_hack = np.zeros((env.size, env.size))

for episode in range(NUM_EPISODES):
    total_reward = 0
    state = env.reset()
    done = False
    steps = 0

    while not done and steps < MAX_STEPS:
        action = agent.select_action(state)
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state)
        state = next_state
        total_reward += reward
        steps += 1
        visits_hack[state[0], state[1]] += 1

    rewards_hack.append(total_reward)
    print(f"Episode {episode + 1}: Total Reward = {total_reward}")

    if detect_reward_hacking(agent, rewards_hack):
        print("⚠️ Reward hacking behavior detected!")

# Plot and save reward curve (with hack)
plt.figure()
plot_rewards(rewards_hack, title='Reward per Episode (With Hack)')
plt.savefig('reward_with_hack.png')
print('✅ Saved: reward_with_hack.png')

# Plot and save heatmap (with hack)
plt.figure()
plt.imshow(visits_hack, cmap='hot', interpolation='nearest')
plt.title('Tile Visit Heatmap (With Hack)')
plt.colorbar(label='Visit Frequency')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.scatter(2, 2, s=200, c='cyan', marker='X', label='Reward Hack')
plt.legend()
plt.savefig('heatmap_with_hack.png')
print('✅ Saved: heatmap_with_hack.png')
