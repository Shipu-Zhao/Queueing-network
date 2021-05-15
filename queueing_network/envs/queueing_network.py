import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class QueueNetEnv(gym.Env):
    
    metadata = {'render.modes': ['human']}

    def __init__(self, config):
        
        self.nu = config['nu']
        self.N = config['N']
        self.alpha = config['alpha']
        self.c = config['c']
        self.starting_state = config['starting_state']

        # Normalization factor for the uniformization
        self.B = round(self.alpha + np.sum(self.nu), 1)

        # Defines state and action spaces, sets current state to be starting_state
        self.action_space = gym.spaces.MultiBinary(4)
        self.observation_space = gym.spaces.MultiDiscrete([self.N+1, self.N+1, self.N+1, self.N+1])
        self.state = self.starting_state
    
    
    def step(self, action):
        reward = self.r(self.state)
        
        probs = [self.transition(action, 0, self.state), self.transition(action, 1, self.state), self.transition(action, 2, self.state), 
                 self.transition(action, 3, self.state), self.transition(action, 4, self.state), self.transition(action, 5, self.state)]
        
        new_transition = np.random.choice(6, p = probs)
        
        New = self.newstate(self.state, new_transition)
        
        self.state = New
        
        episode_over = False

        return self.state, reward, episode_over, {}
        
    
    def reset(self):
        self.state = self.starting_state
        return self.state
    
    
    def indicator_0(self, s):
        if s == 0:
            return 0
        else:
            return 1
    
    def indicator_N(self, s):
        if s == self.N:
            return 0
        else:
            return 1
        
    def transition(self, action, transition, s):
    
        p0 = self.alpha/self.B * self.indicator_N(s[0])   
        p1 = self.nu[0]/self.B * action[0] * self.indicator_0(s[0]) * self.indicator_N(s[1])
        p2 = self.nu[1]/self.B * action[1] * self.indicator_0(s[1]) * self.indicator_N(s[2])
        p3 = self.nu[2]/self.B * action[2] * self.indicator_0(s[2]) * self.indicator_N(s[3])
        p4 = self.nu[3]/self.B * action[3] * self.indicator_0(s[3]) 
    
        if transition == 0:
            p = p0
        elif transition == 1:
            p = p1
        elif transition == 2:
            p = p2
        elif transition == 3:
            p = p3
        elif transition == 4:
            p = p4
        elif transition == 5:
            p = 1 - p0 - p1 - p2 - p3 - p4
    
        return p
    
    def r(self, s):
        return -np.inner(s, self.c)/self.B

    def newstate(self, s, transition):
        new = np.zeros(4)
        new[:] = s[:]
    
        if transition == 0:
            new[0] = s[0] + self.indicator_N(s[0])

        elif transition == 1:
            new[0] = s[0] - self.indicator_0(s[0]) * self.indicator_N(s[1])
            new[1] = s[1] + self.indicator_0(s[0]) * self.indicator_N(s[1])
        
        elif transition == 2:
            new[1] = s[1] - self.indicator_0(s[1]) * self.indicator_N(s[2])
            new[2] = s[2] + self.indicator_0(s[1]) * self.indicator_N(s[2])
        
        elif transition == 3:
            new[2] = s[2] - self.indicator_0(s[2]) * self.indicator_N(s[3])
            new[3] = s[3] + self.indicator_0(s[2]) * self.indicator_N(s[3])
        
        elif transition == 4:
            new[3] = s[3] - self.indicator_0(s[3]) 
    
        return new
