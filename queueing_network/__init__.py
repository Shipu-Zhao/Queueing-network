from gym.envs.registration import register

register(
    id='queueing-network-v0',
    entry_point='queueing_network.envs.queueing_network:QueueNetEnv',
)
