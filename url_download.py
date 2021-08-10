# -*- coding: utf-8 -*-
'''
    Author : Choi hey min
    
    최종 수정일 : 2021.07.08
    
    url download code
    nc file read

'''

import urllib
from urllib.request import urlretrieve
import numpy as np   
import os
from netCDF4 import Dataset, date2index
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from datetime import datetime
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1 import make_axes_locatable

# nc file read

f_name = '2018.nc'

if os.path.isfile(f_name):
    dataset = Dataset(f_name)
    
    print(dataset.title)
    lat = dataset.variables['lat'][:]
    lon = dataset.variables['lon'][:]
    time = dataset.variables['time'][:]
    sst = dataset.variables['sst']


ar_lat= np.array(lat)
ar_lon = np.array(lon)


korea_lat = ar_lat[491: 532]
korea_lon = ar_lon[495:528]



date = datetime(2018,8,10,0)
# draw research area
timevar = dataset.variables['time']
timeindex = date2index(date,timevar) # find time index for desired date.
# read sst.  Will automatically create a masked array using
# missing_value variable attribute. 'squeeze out' singleton dimensions.
sst = dataset.variables['sst'][timeindex,:].squeeze()

# read lats and lons (representing centers of grid boxes).
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
lons, lats = np.meshgrid(lons,lats)

# create figure, axes instances.
fig = plt.figure(figsize=(20, 16))
ax = fig.add_axes([0.05,0.05,0.9,0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)

m = Basemap(llcrnrlon=120,
            llcrnrlat=32,
            urcrnrlon=133,
            urcrnrlat=42,
            lat_0=(42 - 32)/2,
            lon_0=(133-120)/2,
            projection='merc',
            resolution = 'f'
            )

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')

# plot sst
im1 = m.pcolormesh(lons,lats,sst,shading='gouraud',cmap='RdBu_r',latlon=True)

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# add colorbar
cmap = plt.get_cmap('coolwarm')
im1.set_clim(vmin=20, vmax=30)
levels = np.arange(20, 30+1, 2, dtype='int')
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='3%', pad=0.2)
cbar = plt.colorbar(im1, ticks=levels, cax=cax, extend='both')
cbar.set_label(label='SST(℃)', labelpad=20)
    
# add a title.
ax.set_title('SST analysis for %s'%date)
plt.show()
     


# fig = plt.figure(figsize=(16,9))
# ax = fig.add_subplot(111)
# cont = plt.contourf(lon-180, lat, sst, levels=300, cmap="RdBu_r",vmin=-5,vmax=35)
# plt.title('OISSTv2 1982~2010 Sea Surface Temperature',fontweight='bold',fontsize=16)
# plt.xlabel('Longitude',fontsize=13,fontweight='bold')
# plt.ylabel('Latitude',fontsize=13,fontweight='bold')

# v=np.linspace(-5,35,9)
# axins = inset_axes(ax,
#                    width="5%", # width = 10% of parent_bbox width
#                    height="10%", # height : 50%
#                    loc=3,
#                    bbox_to_anchor=(0.02, 0.04, 7, 0.27),
#                    bbox_transform=ax.transAxes,
#                    borderpad=0,
#                    )
# clb=plt.colorbar(cont,cax=axins,orientation='horizontal',
#                  ticks=v, norm=mpl.colors.Normalize(vmin=-5, vmax=35))       

'''
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
    
 '''   