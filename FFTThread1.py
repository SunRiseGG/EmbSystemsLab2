import threading
import time
import math

class FFTThread1(threading.Thread):
    def __init__(self, x, F_Re, F_Im):
        threading.Thread.__init__(self)
        self.x = x
        self.N = len(x)
        self.F_Re = F_Re
        self.F_Im = F_Im

    def run(self):
        print('Starting thread1 for fft')
        res = self.calculate()
        if(res):
            print('Finished thread1 for fft')
            return res

    def calculate(self):
        F_Re1 = []
        F_Im1 = []
        F_Re2 = []
        F_Im2 = []

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

            self.F_Re[p] = F_Re2[p] + F_Re1[p] * math.cos(2 * math.pi * p / self.N)
            self.F_Im[p] = F_Im2[p] + F_Im1[p] * math.sin(2 * math.pi * p / self.N)
        return self.F_Re
