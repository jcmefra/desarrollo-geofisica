#Import dependencies
from pygimli.physics import ert

#Load data
data = ert.load('Guapota_Res.dat')

#Show apparent resistivity data
ax, cb = ert.show(data)

#Compute geometric factor and error
data["k"] = ert.geometricFactors(data)
data["err"] = ert.estimateError(data, relativeError=0.02, absoluteUError=50e-6)

#Initialize ERTManager and run inversion
mgr = ert.ERTManager(data, verbose = True)

inv = mgr.invert()

#Show inversion and apparent resistivity (subplots)
ax, cb = mgr.showResultAndFit()