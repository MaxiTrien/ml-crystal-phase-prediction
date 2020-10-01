import os 
import shutil

path = "C:/Python/Projects/Thesis/data_phase/CIFs"
names = os.listdir(path)

folder_name = ['/HfO2'] 
for x in range(0, len(folder_name)):
    if not os.path.exists(os.sep.join(path, folder_name[x])):
        os.makedirs(os.sep.join(path, folder_name[x])

for files in names:
    if 'HfO2' in files and not os.path.exists(os.sep.join(path, '/HfO2/', files)):
        shutil.move(path + files , path + 'HfO2/' + files) 


filtered_df = df[(df['host'] == 'HfO2') & (df['phase'] == 'm')]