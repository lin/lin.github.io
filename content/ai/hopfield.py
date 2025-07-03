import numpy as np

# Neural networks can store and retrieve patterns via energy minimization and associative memory.
# networks can perform memory, recall, and pattern completion
# 
class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.n = num_neurons
        self.weights = np.zeros((self.n, self.n))

    def train(self, patterns):
        for p in patterns:
            p = p.reshape(self.n, 1)
            self.weights += p @ p.T
        np.fill_diagonal(self.weights, 0)
        self.weights /= self.n  # Optional scaling

    def sign(self, x):
        return np.where(x >= 0, 1, -1)

    def recall(self, pattern, steps=5, verbose=True):
        s = pattern.copy()
        for _ in range(steps):
            for i in range(self.n):
                h_i = np.dot(self.weights[i], s)
                s[i] = self.sign(h_i)
            if verbose:
                print(f"Step {_+1}, state: {s}, Energy: {self.energy(s)}")
        return s

    def energy(self, state):
        return -0.5 * state @ self.weights @ state.T

# Define patterns
pattern1 = np.array([1, -1, 1, -1])
pattern2 = np.array([-1, -1, 1, 1])

# Create and train network
net = HopfieldNetwork(num_neurons=4)
net.train([pattern1, pattern2])

# Create a noisy version of pattern1
noisy = np.array([1, -1, -1, -1])
print("Noisy input:", noisy)

# Recall (recover original pattern)
recovered = net.recall(noisy, steps=15)
print("Recovered pattern:", recovered)
