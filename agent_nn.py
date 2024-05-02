import torch
import torch.nn as nn
import torch.nn.functional as F

class AgentNetwork(nn.Module):
    def __init__(self, obs_shape, num_actions):
        super(AgentNetwork, self).__init__()

        self.fc1 = nn.Linear(obs_shape, 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, num_actions)

        self.fc4 = nn.Linear(256, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        value = self.fc4(x)

        return x, value

class Agent:
    def __init__(self):
        obs_shape = 81
        num_actions = 4
        self.actor = AgentNetwork(obs_shape, num_actions)

    def act(self, state):
        state = torch.tensor(state, dtype=torch.float32)
        action, _ = self.actor(state)
        action = action.detach().numpy()
        return action
