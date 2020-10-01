from ase.io import read
from ase.visualize import view
from ase.spacegroup import crystal
from crystals import Crystal
import matplotlib.pyplot as plt
import numpy as np
from skued import powdersim
#from skued import Crystal

filename1 = r"C:\Users\Maxi\Desktop\pure_HfO2_t.cif"
filename2 = r"C:\Users\Maxi\Desktop\Li_HfO2_inter_6.25_221_t.cif"



# load cif file to an ase object
s = read(filename1)
s2 = read(filename2)
s1 = crystal(s)

# crystal object for powdersim in skued lib
crys = Crystal.from_ase(s1)
pure_cry = Crystal.from_ase(s2)

# visualize crystal 
view(s)
#print(s.get_positions())
#print(s.get_atomic_numbers())
#print(s.get_cell()[:])

# powder simulation with range of q 
q = np.linspace(1, 7, 512)
diff1 = powdersim(crys, q)
diff2 = powdersim(pure_cry, q)

# diff1 = powdersim(cry1, q, fwhm_g=0.01, fwhm_l=1)
# diff2 = powdersim(cry2, q, fwhm_g=0.01, fwhm_l=1)

# matplotlib config
plt.figure()
plt.plot(q, diff1/diff1.max(), '-b', label='dotant', alpha= 0.3)
plt.plot(q, diff2/diff2.max(), '-r', label='pure', alpha= 0.3)
plt.legend()
plt.xlim([q.min(), q.max()])
plt.xlabel('$q (1/\AA)$')
plt.ylabel('Diffracted intensity (A.u.)')
plt.title('Crystal diffraction ')
plt.show()