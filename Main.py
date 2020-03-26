from RandomSignal import RandomSignal
from time import perf_counter
from DFT import DFT
from FFT import FFT
import matplotlib.pyplot as plt

class Main:
    n = 14
    w = 2500
    N = 64

    randomSignalTime1 = perf_counter()
    obj = RandomSignal(n, w, N)
    points = obj.generete_signal()
    randomSignalTime2 = perf_counter()
    randomSignalTime = randomSignalTime2 - randomSignalTime1;

    randomSignalPoints = []
    for i in range(len(points)):
        randomSignalPoints.append(points[i][1])

    fft = FFT(randomSignalPoints)
    dft = DFT(randomSignalPoints)

    dftTime1 = perf_counter()
    dftPoints = fft.calculate()
    dftTime2 = perf_counter()
    dftTime = dftTime2 - dftTime1

    fftTime1 = perf_counter()
    fftPoints = dft.calculate()
    fftTime2 = perf_counter()
    fftTime = fftTime2 - fftTime1
    print(randomSignalTime, dftTime, fftTime)

    plt.plot([x for x in range(N)], dftPoints, color='orange')
    plt.plot([x for x in range(N)], fftPoints, color='r')
    plt.show()
