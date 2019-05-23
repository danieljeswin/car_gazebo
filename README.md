# car_gazebo
My implementation of a simple 4 wheel vehicle with ROS

## Getting Started
Simply clone the repo, compile and make sure you've installed the prerequisites and you're all ready to go.

### Prerequisites
1. ROS Kinetic
2. Gazebo7 - have not tested for compatibility with later versions of Gazebo.

### Running
Clone the repo into a catkin_workspace.
Create workspace using the following commands.

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
```

Once cloned compile using the following commands

```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

To launch the simulation launch the main.launch file using the following command

```
roslaunch car_description main.launch
```

### Description
The package car_description contains the URDF and XACRO description of the vehicle.
The car is controlled by skid steer controller plugin in Gazebo. It can also be controlled using ROS controllers.

For controlling with Gazebo Plugins the transmission tags must be excluded while for ROS control they must be included.
car_description also contains configurations to fuse odometry and imu data for better localization.

The package car_control contains all the configurations and launch files for ROS Control.
Skid Steer controllers as well as velocity controls for each individual wheels are available.

The package car_navigation contains the code for performing autonomous navigation. GMapping is used to generate maps and AMCL algorithm is used for localization.
Two maps have also been generated.

The package circuit contains a basic square circuit used to drive the car for testing.


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
