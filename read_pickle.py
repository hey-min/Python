import pickle

# pickle = [nc_sst, nc_lat, nc_lon, nc_time]

with open('pickle_name.pickle', 'rb') as f:
  nc_sst = pickle.load(f)
  nc_lat = pickle.load(f)
  nc_lon = pickle.load(f)
  nc_time = pickle.load(f)
