import matplotlib.pyplot as plt
import numpy as np
import pygimli as pg
from pygimli.physics import ert
import pygimli.meshtools as mt

data = ert.load('Guapota_Res.dat')


ax, cb = ert.show(data)

data["k"] = ert.geometricFactors(data)
data["err"] = ert.estimateError(data, relativeError=0.02, absoluteUError=50e-6)

mgr = ert.ERTManager(data, verbose = True)

inv = mgr.invert()

ax, cb = mgr.showResultAndFit()
#meshPD = pg.Mesh(mgr.paraDomain) 