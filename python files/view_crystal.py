from ase.io import read
from ase.visualize import view
from ase.spacegroup import crystal
from crystals import Crystal
import matplotlib.pyplot as plt
import numpy as np
from skued import powdersim
from pathlib import Path 


def view_crystal(cif_path):
    # visualize the crystal
    s = read(cif_path)
    view(s, block=True)


def pow_sim(path1):
    filename1 = Path(path1).name
    #filename2 = Path(path2).name    

    # load cif file to an ase object
    cry1 = read(path1)
    #cry2 = read(path2)

    # crystal object for powdersim in skued lib
    crys1 = Crystal.from_ase(cry1)
    #crys2 = Crystal.from_ase(cry2)

    # powder simulation with range of q 
    q = np.linspace(1, 7, 512)
    diff1 = powdersim(crys1, q, fwhm_g = 0.01, fwhm_l=0.03)
    #diff2 = powdersim(crys2, q)

    # matplotlib config
    plt.figure()
    plt.plot(q, diff1/diff1.max(), '-b', label=filename1, alpha= 0.3)
    #plt.plot(q, diff2/diff2.max(), '-r', label=filename2, alpha= 0.3)
    plt.legend()
    plt.xlim([q.min(), q.max()])
    plt.xlabel('$q (1/\AA)$')
    plt.ylabel('Diffracted intensity (A.u.)')
    plt.title('Crystal diffraction ')
    plt.show()

def get_specs_crystal(path):
    # get information of the crystal
    s = read(path)
    position = s.get_positions()
    atomic_number = s.get_atomic_numbers()
    unit_cell = s.get_cell_lengths_and_angles()
    print('Postion:')
    print(position)
    print('Atomic Number:')
    print(atomic_number)
    print('unit cell:')
    print(unit_cell)



path = r'C:\Python\Projects\crystal-phase-prediction\crystal_data\package\Hf14LaO32Si_sc122\No14\11\geometry.in'
# path2 = r"C:\Python\Projects\crystal-phase-prediction\crystal_data\CIFs_pure\pure_HfO2_p-o.cif"

view_crystal(path)
# pow_sim(path1)
get_specs_crystal(path)




