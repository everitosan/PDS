import math as M
class LowPassFilter(object):
  def __init__(self, params):

    # Save params
    self.fp = float(params[0])
    self.fs = float(params[1])
    self.Fs = float(params[2])
    if len(params) == 3:
      self.App = 0.1
    else:
      self.App = float(params[3])

    # Determines fc
    self.fc = float((self.fp + self.fs) / 2)

    # Determines Period
    self.T = 1/self.Fs

    # Determines Number of coefficients
    self.N = self.getNCoefficients()

    #initialice arrays
    self.NonCausal = [0] * self.N
    self.Causal = [0] * self.N

  def getNCoefficients(self):
    deltaF = self.fs - self.fp

    auxDeltaP = M.pow(10, 0.05*self.App)
    deltaP = (auxDeltaP - 1) / (auxDeltaP + 1)

    A = -20 * M.log10(deltaP)
    D = (A - 7.95) / 14.36
    N = M.trunc( ((self.Fs * D) / deltaF) + 1)

    if N%2 == 0:
      N+=1

    return N


  def calculateCoefficients(self):
    Fn = 1
    fcn = float(self.fc / self.Fs)

    max = (self.N+1)/2

    h = hd =  [0] * max
    delays = [0] * self.N

    for n in range(0, max):
      if n == 0:
        hd[0] = (2* fcn) / Fn # Formula case n == 0
      else:
        hd[n] = (1/ (M.pi*n)) * (M.sin( 2 * M.pi *fcn*n*Fn)) # Formula n != 0

      ah = 0.54 + (0.46 * M.cos( ( 2*M.pi*n ) / ( self.N-1 ) ))
      h[n]= hd[n]*ah 

    return h


  def fixCoef(self):
    auxCoeff = [0] * self.N

    arrLen = len(self.NonCausal)
    half = (self.N - 1) / 2

    for n in range(0, arrLen):
      if n == 0:
        auxCoeff[half] = self.NonCausal[0]
      else :
        auxCoeff[half-n] = self.NonCausal[n]
        auxCoeff[half+n] = self.NonCausal[n]
      
    return auxCoeff

  def calc(self):
    self.NonCausal = self.calculateCoefficients()
    self.Causal = self.fixCoef()

  def getN(self):
    return self.N
    
  def getNonCausalCoeff(self):   
    return self.NonCausal


  def getCausalCoeff(self):
    return self.Causal



