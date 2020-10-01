from ase.io import read
from ase.visualize import view
import os 
import numpy as np
import pandas as pd


folder = r"C:\Python\Projects\Thesis\data_phase\CIFs"
arr = os.listdir('data_phase\CIFs')

filename_arr = []
angle_length_arr = []

# loop throuth the .cif files and get data arrays
for file in arr:
    filename = os.sep.join([folder, file])
    cristal = read(filename)
    filename_arr.append(file)
    angle_length = list(cristal.get_cell_lengths_and_angles())
    angle_length_arr.append(angle_length)


# replace .cif in the filenames
filename_arr_short = []
for name in filename_arr:
    name = name.replace('.cif', '')
    filename_arr_short.append(name)

# split the name in the title into different features
ext_features = []
for name in filename_arr:
    name = name.replace('.cif', '')
    name_list = name.split('_')
    ext_features.append(name_list)

    
    
# convert list to arrays 
filename_arr_short = np.array(filename_arr_short)
angle_length_arr = np.array(angle_length_arr)
ext_features = np.array(ext_features)
df_array = np.concatenate((ext_features, angle_length_arr),axis=1)

# form arrays to a pandas dataframe
name = ['dopant','chem_comp.','dopant_pos.','f.u.%','size_unit_cell','phase','a', 'b', 'c', 'alpha', 'beta', 'gamma']
df = pd.DataFrame(df_array, columns=name)
df.insert(0, 'probe', filename_arr_short, True)


# search for different data in dataframe
# filtered_df = df[(df['probe'].str.contains('m') & (df['probe'].str.contains('HfO2')))]

print(df)
df.to_pickle('probe_data.pkl')


"""
s = read(filename)
view(s)
# print(s.get_positions())
atomic_number = s.get_atomic_numbers()
unit_cell = s.get_cell()[:]

print(atomic_number)
print(unit_cell)
 """
