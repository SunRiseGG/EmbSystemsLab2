from RandomSignal import RandomSignal
import math

class FFT(RandomSignal):
    def __init__(self, x):
        self.x = x
        self.N = len(x)

    def calculate(self):
        F_Re1 = []
        F_Im1 = []
        F_Re2 = []
        F_Im2 = []
        F_Re = [None] * self.N
        F_Im = [None] * self.N

        for p in range(int(self.N / 2)):
            F_Re1.append(0.0)
            F_Im1.append(0.0)
            F_Re2.append(0.0)
            F_Im2.append(0.0)

            for m in range(int(self.N / 2)):
                F_Re1[p] += self.x[2 * m + 1] * math.cos(4 * math.pi * p * m / self.N)
                F_Re2[p] += self.x[2 * m] * math.cos(4 * math.pi * p * m / self.N)
                F_Im1[p] -= self.x[2 * m + 1] * math.sin(4 * math.pi * p * m / self.N)
                F_Im2[p] -= self.x[2 * m] * math.sin(4 * math.pi * p * m / self.N)

            F_Re[p] = F_Re2[p] + F_Re1[p] * math.cos(2 * math.pi * p / self.N)
            F_Re[p + int(self.N / 2)] = F_Re2[p] + F_Re1[p] * math.cos(2 * math.pi * (p + self.N / 2) / self.N)
            F_Im[p] = F_Im2[p] + F_Im1[p] * math.sin(2 * math.pi * p / self.N)
            F_Im[p + int(self.N / 2)] = F_Im2[p] + F_Im1[p] * math.sin(2 * math.pi * (p + self.N / 2) / self.N)
        return F_Re
