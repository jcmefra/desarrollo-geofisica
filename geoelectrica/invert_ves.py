import numpy as np
import pygimli as pg
from pygimli.physics import VESManager

txt = np.loadtxt('sev_2.sdg.TXT', delimiter='\t', skiprows=1) #Import txt, csv or file with the data
ab2 = (txt[:,0])  # AB/2 distance (current electrodes)
mn2 = [mn/2 for mn in (txt[:,1])]
rhoa = (txt[:,6])

ves = VESManager()
# %%%
ves.invert(data=rhoa, error=0.1, ab2=ab2, mn2=mn2,
           nLayers=4,
           # startModel=[3]*3+[100]*4,
           lam=1000, lambdaFactor=0.8
           )

# %%%
# show estimated&synthetic models and data with model response in 2 subplots
fig, ax = pg.plt.subplots(ncols=2, figsize=(8, 6))  # two-column figure
#ves.showModel(synthModel, ax=ax[0], label="synth", plot="semilogy", zmax=20)
ves.showModel(ves.model, ax=ax[0], label="model", zmax=200)
ves.showData(rhoa, ax=ax[1], label="data", color="C0", marker="x")
ves.showData(ves.inv.response, ax=ax[1], label="response", color="C1")