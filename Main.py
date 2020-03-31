from RandomSignal import RandomSignal
from FFTThread1 import FFTThread1
from FFTThread2 import FFTThread2
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

    F_Re = [None] * len(randomSignalPoints)
    F_Im = [None] * len(randomSignalPoints)
    fftThread1 = FFTThread1(randomSignalPoints, F_Re, F_Im)
    fftThread2 = FFTThread2(randomSignalPoints, F_Re, F_Im)
    fft = FFT(randomSignalPoints)
    dft = DFT(randomSignalPoints)

    dftTimeStart = perf_counter()
    dftPoints = dft.calculate()
    dftTimeFinish = perf_counter()
    dftTime = dftTimeFinish - dftTimeStart

    fftTimeStart = perf_counter()
    fftPoints = fft.calculate()
    fftTimeFinish = perf_counter()
    fftTime = fftTimeFinish - fftTimeStart

    fftTimeThreadsStart = perf_counter()
    fftPoints1 = fftThread1.start()
    fftPoints2 = fftThread2.start()
    fftTimeThreadsFinish = perf_counter()
    fftTimeThreads = fftTimeThreadsFinish - fftTimeThreadsStart

    print(randomSignalTime, dftTime, fftTime, fftTimeThreads)

    plt.plot([x for x in range(N)], dftPoints, color='orange')
    plt.plot([x for x in range(N)], fftPoints, color='r')
    plt.show()
