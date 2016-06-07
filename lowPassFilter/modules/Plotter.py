import matplotlib.pyplot as pyPlot
import math as M
import numpy as np

class Plotter(object):
  def setNPlot(self, n):
    self.nPlot = n
    self.indexPlot = 1

  def addPlot(self, data, type = "DATA"):
    index = self.nPlot * 100 + 10 + self.indexPlot
    pyPlot.subplot(index)
    if type == "DATA":
      pyPlot.plot(data[0], data[1])
    elif type == "FREQ_RESPONSE":
      freq_res = self.frequencyResponse(data[0])
      pyPlot.plot(freq_res[0]*8000, freq_res[1], data[1])
    pyPlot.xlabel(data[2])
    self.indexPlot+=1

  def frequencyResponse(self, h):
    index = 0
    N = len(h)
    array = np.arange(0, .5, 0.007)
    dB = [0] * len(array)

    for f in array:
      freq_response = 0
      
      for n in range(1, N, 1):
        mCos = M.cos(2*M.pi*f*n)
        freq_response = freq_response + (h[n] * mCos)

      dB[index] = 20*M.log10(M.fabs(h[0]+(2*freq_response)))
      index += 1 
    
    return [array, dB]

  def show(self):
    pyPlot.show()