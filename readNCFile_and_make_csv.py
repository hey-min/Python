from netCDF4 import Dataset
import pandas as pd
import numpy as np
import os

file_name = 'nc_name.nc'

fh = Dataset(file_name)

print('================= NC File Group List =================')
print(fh)
for item in fh.groups:
    print('==================='+item+'===================')
    print(fh[item])

# check fh['group_name']['variables'][...][...]
# check fh variables

# make file_list[] from folder_path 
folder_path = '...'
file_list = []
if os.path.isdir(folder_path):
    for file in os.listdir(folder_path):
        # file name end with 'GEO.nc'
        if file.endswith('GEO.nc'):
            file_list.append(file)

# sample nc file name
nc_file = 'GK2B_GOCI2_L2_20210404_201630_FD_S000_G065_GEO.nc'

# make csv file from file_list[]'s value
csv_file_name= 'READ_GEO_NC.csv'
columns = ['nc_file', 'rslt']
df = pd.DataFrame(data=None, columns=columns)

for nc_file in file_list:
    # fh groups: geophysical_data, navigation_data
    fh = Dataset(folder_path+nc_file)

    # ex) float SolZ_490(number_of_lines=3100, pixels_per_line=3100);
    number_of_lines = 1553
    pixels_per_line = 1551
    # ex) group(geophysical_data)>variable(SolZ)>variable(SolZ_490)
    rslt = fh['geophysical_data']['SolZ']['SolZ_490'][number_of_lines][pixels_per_line]
    
    new_data = pd.DataFrame([{'nc_file': nc_file,
                              'rslt': rslt}])
    
    df = df.append(new_data)
    
df.index = np.arange(1, len(file_list)+1)
print(df.tail(3))

# save csv file
csv_file = df.to_csv(csv_file_name)


