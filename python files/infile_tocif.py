from ase.io import read, write
from os import listdir
import os
import re


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


def load_path(folder):
    '''
    Load .in files from folder into ase crystal objects
    
    '''
    list_ofpath = getListOfFiles(folder)
    for path in list_ofpath:
        print(path)
    return list_ofpath


def create_cif(direct_path, goal_path):
    names_split= []
    names = []
    for file in direct_path:
        crystal = read(file)
        split_file = list(file.split(os.sep))

        title = split_file[7]+ '_' + split_file[8] + '_' + split_file[9] + '.cif'

        final_path = os.path.join(goal_path, title)
        write(final_path, crystal)
    return 0

  

path_main = r'C:\Python\Projects\crystal-phase-prediction\crystal_data\package\HfLaO' 
goal_path = r'C:\Python\Projects\crystal-phase-prediction\crystal_data\package\hfo2_La'

direct_path = load_path(path_main)
create_cif(direct_path,goal_path)

'''

infile = read(pathfile)

pathfolder_name = r'C:\Python\Projects\crystal-phase-prediction\crystal_data\package\HfLaO'
pathfolder_name_list = listdir(pathfolder_name)
pathfolder_phase = r'C:\Python\Projects\crystal-phase-prediction\crystal_data\package\HfLaO\Hf14La2O32_sc122'
pathfolder_phase_list = listdir(pathfolder_phase)
pathfolder_phase_list = natural_sort(pathfolder_phase_list)
print(pathfolder_phase_list[0])

outputfile = pathfolder_name_list[0] + 'm'+ '_1' + '.cif'
final_folder = r"C:\Python\Projects\crystal-phase-prediction\crystal_data\package\hfo2_La"
target_path = os.sep.join([final_folder, outputfile])

write(target_path, infile)
'''
