# -*- coding: utf-8 -*-
'''
    Author : Choi hey min
    
    최종 수정일 : 2021.02.19
    
    url download code

'''

import urllib
from urllib.request import urlretrieve
import numpy as np   

if __name__ == '__main__':

    file_list = np.arange(2007, 2020) 
    
    
    for list in file_list:
    
        url = 'ftp://ftp2.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.'+str(list)+'.nc'
        
        req = urllib.request.Request(url)
    
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        
        save_name = str(list)+'.nc'
        
        print('{} download start' .format(list))
        urlretrieve(url, save_name)
        
        print('Download {}.nc' .format(list))
    
    