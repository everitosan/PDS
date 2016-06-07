from modules.LowPassFilter import LowPassFilter
from modules.Plotter import Plotter
from time import gmtime, strftime

params = [600, 2000, 8000] # fp, fs, Fs, [App]
mFilter =  LowPassFilter(params)
mPlot = Plotter()

mFilter.calc()

NonCausalcoeff = mFilter.getNonCausalCoeff()
CausalCoeff = mFilter.getCausalCoeff()

fileName = "Filter" +  strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".txt"

file = open (fileName, "w")
for c in CausalCoeff:
  file.write( str(c) +"\n")
file.close()


mPlot.setNPlot(2)
mPlot.addPlot([NonCausalcoeff, "", "RESPUESTA EN FCIA"], "FREQ_RESPONSE")
legend= "COEFICIENTES: " + str(mFilter.getNCoefficients())
mPlot.addPlot([CausalCoeff, "bo", legend])
mPlot.show()



