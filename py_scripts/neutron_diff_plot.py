import Dans_Diffraction as dif
import matplotlib.pyplot as plt
filename1 = r"C:\Python\Projects\crystal-phase-prediction\crystal_data\CIFs\Ag_HfO2_cat_3.125_222_p-o.cif"
# Choose scattering options (see help(xtl.Scatter.setup_scatter))

xtl = dif.Crystal(filename1)


xtl.Scatter.setup_scatter(
    type='xray',
    energy_kev=8,
    )


Q,I = xtl.Scatter.generate_powder(q_max=8, peak_width=0.01, background=0, powder_average=True)
print(I)
print(Q)

plt.figure()
plt.plot(Q, I/I.max() , '-b', alpha= 0.3)

plt.legend()
plt.xlim([Q.min(), Q.max()])
plt.xlabel('$q (1/\AA)$')
plt.ylabel('Diffracted intensity (A.u.)')
plt.title('Crystal diffraction ')
plt.show()

