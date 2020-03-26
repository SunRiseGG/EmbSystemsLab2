from RandomSignal import RandomSignal
import math

class DFT(RandomSignal):
    def __init__(self, x):
        self.x = x
        self.N = len(x)

    def calculate(self):
        F_Re = []
        F_Im = []
        F = []
        w_Re = []
        w_Im = []

        for p in range(self.N):
            w_Re.append([])
            w_Im.append([])
            for k in range(self.N):
                w_Re[p].append(math.cos(2 * math.pi * p * k / self.N))
                w_Im[p].append(math.sin(2 * math.pi * p * k / self.N))

        for p in range(self.N):
            F_Re.append(0.0)
            F_Im.append(0.0)

            for k in range(self.N):
                F_Re[p] += self.x[k] * w_Re[p][k]
                F_Im[p] -= self.x[k] * w_Im[p][k]

            F.append(F_Re[p] * F_Re[p] + F_Im[p] * F_Im[p])
        return F_Re
