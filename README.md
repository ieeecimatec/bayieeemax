# BayIEEEmax
A project in develepment of a openSource health helper robot, developed by the IEEE RAS, IEEE PES and IEEE EMBS CIMATEC Student Chapter. The ROS NOETIC is been used.

## Install the packages
- First, create a ROS workspace:
```bash
$ mkdir -p ~/baymax_ws/src
```
- Clone this repository inside your /src folder:
```bash
$ cd ~/baymax_ws/src
$ git clone git@github.com:ieeecimatec/bayieeemax.git
```
- Build your workspace:
```bash
$ cd ~/baymax_ws
$ catkin_make
```

## Package contents
In development.

## Simulation
When open a new terminal:
```bash
$ cd ~/baymax_ws
$ source devel/setup.bash
```
The bayieeemax_launchs package provides some useful launch files for simulation. 
By default, it will start an empth world, but you can change it if you want.

Also, if you want to make your own launch file, you can be based on the 'template.launch'.