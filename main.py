import STOM_higgs_tools, numpy as np
import matplotlib.pyplot as plt # Making plots.

def function_hist(a, ini, final):

    # 12 bins
    bins = np.linspace(ini, final, 31)
    weightsa = np.ones_like(a)/float(len(a))
    return np.histogram(np.array(a), bins, weights = weightsa)

vals = np.asarray(STOM_higgs_tools.generate_data())
bin_heights, bin_edges = function_hist(vals,104, 155)
plt.errorbar((bin_edges[0:-1:]+bin_edges[1::])/2,bin_heights*len(vals),np.sqrt(bin_heights*len(vals)),ls="none")
plt.show()
