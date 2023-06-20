import numpy as np

class Vehicle:
    def __init__(self, v_max, a, b, T, s_0, delta):
        self.v_max = v_max
        self.a = a
        self.b = b
        self.T = T
        self.s_0 = s_0
        self.delta = delta
        self.v = 0
        self.s = 0

    def update(self, v_front, s_front, dt):
        s_star = self.s_0 + max(0, self.v*self.T + self.v*(self.v - v_front)/(2*np.sqrt(self.a*self.b)))
        epsilon = 1e-10  # small constant to prevent division by zero
        self.v += dt*(self.a*(1 - (self.v/self.v_max)**self.delta - (s_star/(self.s + epsilon))**2))
        self.s += self.v*dt
        return self.v, self.s