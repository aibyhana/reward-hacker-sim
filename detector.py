"# Simple reward-hacking detector" 
def detect_reward_hacking(agent, reward_history):
    if len(reward_history) < 10:
        return False

    last_10 = reward_history[-10:]
    avg_recent = sum(last_10) / 10
    if avg_recent > 10:
        return True

    hacked_tile_visits = [s for (s, a) in agent.q_table.keys() if s == (2, 2)]
    if len(hacked_tile_visits) > 10:
        return True

    return False

