import matplotlib.pyplot as plt
import numpy             as np
import csv
from numpy import genfromtxt
from matplotlib import cm

traj_data = genfromtxt('../example-data/hockenheim/practice-trackdrive-v10/path.csv', delimiter=',')
path_data = genfromtxt('../example-data/hockenheim/practice-trackdrive-v10/t3_tp.log', delimiter=',')
blue_cones_data = genfromtxt('../example-data/hockenheim/practice-trackdrive-v10/blue_cones.csv', delimiter=',')
yellow_cones_data = genfromtxt('../example-data/hockenheim/practice-trackdrive-v10/yellow_cones.csv', delimiter=',')

fig, ax = plt.subplots(figsize=(16,16))

x_traj_pos = []
y_traj_pos = []
vx_traj    = []
steering_traj   = []
yaw_traj        = []
slip_traj       = []
yaw_rate_traj   = []


# x_pos, y_pos, vx[m/s], steering[rad], yaw[rad], slip[rad], yaw_rate[rad/s]
#
for frame in traj_data:
    x_pos    = frame[0]
    y_pos    = frame[1]
    vx       = frame[2]
    steering = frame[3]
    yaw      = frame[4]
    slip     = frame[5]
    yaw_rate = frame[6]
    
    x_traj_pos = np.append(x_traj_pos, x_pos)
    y_traj_pos = np.append(y_traj_pos, y_pos)
    vx_traj       = np.append(vx_traj, vx)
    steering_traj = np.append(steering_traj, steering)
    yaw_traj      = np.append(yaw_traj, yaw)
    slip_traj     = np.append(slip_traj, slip)
    yaw_rate_traj = np.append(yaw_rate_traj, yaw_rate)

x = np.arange(0, len(x_traj_pos))

ax.scatter( x_traj_pos, y_traj_pos, s = 25, color = cm.viridis(vx_traj), label = 'planned trajectory', edgecolor='none' );


path_x, path_y = unzip(path_data)

ax.scatter(path_x, path_y)

#plt.ylim(-2,2,0.5)

#plt.plot(acc_data_dark, label = 'yaw_rate is')
plt.legend()
plt.grid()
plt.show()