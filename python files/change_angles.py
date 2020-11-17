"""
@author: Maxi

We want to change the hfo2 or zro2 angles to 90/80 deg.
 and see if it has an impact on the clearness of 
clustering. 
"""


from ase.io import read, write
import os


def change_angles(folder, target_folder, arr):
    '''
    Load cif files from folder into ase crystal objects, change 
    all elements O with specific other elements.
    '''
    filename_arr = []
    j = 0
    for file in arr:
        filename = os.sep.join([folder, file])
        filename_arr.append(file)
        crystal = read(filename)
        unit_cell = crystal.get_cell_lengths_and_angles()
        i = 3
        for angle in unit_cell[3:6]:
            if(75.0 <= angle <= 85.0):
                unit_cell[i] = 80.0
            else:
                unit_cell[i] = 90.0
            i = i + 1
        
        crystal.set_cell(unit_cell)
        print(crystal.get_cell_lengths_and_angles())
        print(j)
        target_path = os.sep.join([target_folder, file])
        write(target_path, crystal)
        j = j + 1


folder = r'C:\Python\Projects\crystal-phase-prediction\crystal_data\hfo2' # load data from this folder 
arr = [f for f in os.listdir(folder) if not f.endswith('.ini')] # ignore hidden files in folder
target_folder = r'C:\Python\Projects\crystal-phase-prediction\crystal_data\hfo2_90_80_deg' # file where to store the new cif files

change_angles(folder, target_folder, arr)
