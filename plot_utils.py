"# Optional: plots rewards/actions" 
import matplotlib.pyplot as plt

def plot_rewards(rewards, title='Reward per Episode'):
    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title(title)
    plt.grid(True)
