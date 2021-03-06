import matplotlib.pyplot as plt
import numpy             as np
import csv
from numpy import genfromtxt

traj_data = genfromtxt('../example-data/hockenheim/skidpad-v02/middle.csv', delimiter=',')
path_data = genfromtxt('../example-data/hockenheim/skidpad-v02/skipa_debug.log', delimiter=',')

fig, ax = plt.subplots(figsize=(16,16))

x_traj_pos = []
y_traj_pos = []

#
for frame in traj_data:
    x_pos    = frame[0]
    y_pos    = frame[1]
    
    x_traj_pos = np.append(x_traj_pos, x_pos)
    y_traj_pos = np.append(y_traj_pos, y_pos)


x_path_pos = []
y_path_pos = []
local_path_found = []
#
for frame in path_data:
    x_pos    = frame[0]
    y_pos    = frame[1]
#    local_path = frame[8]    
    x_path_pos = np.append(x_path_pos, x_pos)
    y_path_pos = np.append(y_path_pos, y_pos)
#    local_path_found = np.append(local_path_found, local_path)


ax.scatter( x_traj_pos, y_traj_pos, s = 2.5, color = '#7ddc1f', label = 'planned trajectory' );

#counter = 0
#for x_path, y_path, path_found in zip(x_path_pos, y_path_pos, local_path_found):
#    #if counter %  
#    if (path_found == '1'):
color = '#ff6347'
#    else:
#        color = '#ff1053'
ax.scatter( x_path_pos , y_path_pos, s = 2.5, color = color, label = 'driven path' );



#plt.ylim(-2,2,0.5)

#plt.plot(acc_data_dark, label = 'yaw_rate is')
plt.legend()
plt.grid()
plt.show()