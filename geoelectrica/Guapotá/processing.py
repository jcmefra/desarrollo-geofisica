# %% [markdown]
# Import dependencies

# %%
import matplotlib.pyplot as plt
import numpy as np
import pygimli as pg
from pygimli.physics import ert

# %% [markdown]
# Load ERT Data (Res2Dinv converted from FlashResZZ)

# %%
data = ert.load('Guapota_Res.dat')
print(data)

# %% [markdown]
# Show pseudosection

# %%
ax, cb = ert.show(data)

# %% [markdown]
# Compute geometric factors

# %%
data["k"] = ert.geometricFactors(data)
data["err"] = ert.estimateError(data, relativeError=0.02, absoluteUError=50e-6)
mgr = ert.ERTManager(data, verbose=True)
mgr.invert()

# %% [markdown]
# Define colormap and plot inversion

# %%
kw = dict(logScale=True, cMap="Spectral_r", xlabel="x (m)", ylabel="y (m)")
ax, cb = mgr.showResult(**kw)
ax.grid(True)


