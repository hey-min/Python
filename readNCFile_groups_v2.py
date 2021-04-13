


from netCDF4 import Dataset
import pandas as pd
import numpy as np
import os

file_name = '2007to2019.nc'

fh = Dataset(file_name)

print('================= NC File Group List =================')
for item in fh.groups:
    print('==================='+item+'===================')
    print(fh[item])

# date = '20210405'
# folder_path = '//10.108.0.221/g2gs/2021/04/05/FD_L2/V1.0.0/GK2_GC2_L2_'+str(date)+'_201630_FD/'
# csv_file_name= 'READ_GEO_NC.csv'

# file_list = []
# if os.path.isdir(folder_path):
    
#     for file in os.listdir(folder_path):
        
#         if file.endswith('GEO.nc'):
#             file_list.append(file)


# nc_file = 'GK2B_GOCI2_L2_20210404_201630_FD_S000_G065_GEO.nc'

# columns = ['nc_file', 'rslt']
# df = pd.DataFrame(data=None, columns=columns)

# for nc_file in file_list:
#     # fh groups: geophysical_data, navigation_data
#     fh = Dataset(folder_path+nc_file)

#     # float SolZ_490(number_of_lines=3100, pixels_per_line=3100);
#     number_of_lines = 1553
#     pixels_per_line = 1551
#     rslt = fh['geophysical_data']['SolZ']['SolZ_490'][number_of_lines][pixels_per_line]
    
#     new_data = pd.DataFrame([{'nc_file': nc_file,
#                              'rslt': rslt}])
    
#     df = df.append(new_data)
    
# df.index = np.arange(1, len(file_list)+1)
# print(df.tail(3))

# csv_file = df.to_csv(csv_file_name)