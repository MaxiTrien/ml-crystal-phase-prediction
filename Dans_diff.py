import Dans_Diffraction as dif
import matplotlib as plt
import numpy as np

xtl = dif.Crystal('')
#print(xtl.info())
arr = xtl.Scatter.print_all_reflections(energy_kev=8)
xtl.Plot.simulate_powder(energy_kev=8)

xtl.start_gui()
