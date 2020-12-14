![Capture3](https://user-images.githubusercontent.com/69988399/102021689-8c1a8580-3d92-11eb-9ff6-c8b26122f97c.JPG)


<h1 align="center"> Robotics Project
<h3 align="center"> Supervisors:
<h3 align="center"> Raphael DUVERNE, Daniel BRAUN & Ralph SEULIN
<h3 align="center"> students: 
<h3 align="center"> Vasileios Melissianos and Ahmed Hossameldin











# Introduction
 ROS (Robot Operating System) is one of the best ways to control any robot (mobile robots, robotic arms est..) and that because of ROS is an open-source, meta-operating system. This gives the services you would expect from an operating system, such as abstraction of hardware, low-level device control, widely-used functionality implementation, message-passing between systems, and package management. It also offers tools and libraries on multiple computers to obtain, create, write, and run code.
 
This project is to execute four tasks using TurtleBot 3 mobile robot and simulation performing them on  [The Construct](https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/) Web Platform.

### Project challenges

 - Create a script that moves the robot around with simple /cmd_vel topic publishing.
 - Generate the full map of the cafeteria and then localize the Turtlebot3 robot.
 - Set up an automatic system that provides the robot to move from its position to a goal without colliding with any object.
 - Set up an automatic system that provides the robot to move from its position to a set of waypoints.

## ROS materials
In this section, in order to accomplish these tasks, the use of these materials is necessary. The combination of these materials composes the appropriate package for a specific task. Thus, these components are summarized below:

 - Packages: A package is a set of information that acts as an independent library for a specific task. Precisely, a package provides a set of scripts, launch files, maps, configuration files, in order to get/give information from/to ROS nodes and thus, provide a fully functional system for a specific task. A package provides:
 1. Launch folder
 Launch files: A launch file is a script that replaces the console commands and composes an automatic system that monitors all the file inside a package.
 2. Script folder
 Scripts: A script is an executable file used for accomplishing a task.
 3. Maps-Configuration:
Maps: Map files that have been generated for Robot navigation tasks.
Configuration: The map’s parameters and also the parameters of the sensor used for map generation.
 5. Package.xml: 
 This unique file contains a set of different packages to create a more customizable package (if necessary).
 6. CMakeLists.txt:
This unique file contains some C++ fixed processes and building commands. This file is necessary for building a package.

- Nodes: A node is a built-in ROS function (python, C++) that provides/gets information from ROS topics. ROS nodes can subscribe or publish to a topic for the purpose of sharing important information such as metric values etc.
-	Topics: A topic is the most important component in the package. It can transmit data between nodes (e.g. one node provides values to the topic, and another node prints the topic’s values) and can provide data throughout ROS built-in sensors, functions etc.
-	Messages: A message is a data structure provided by a ROS node using a specific topic. These values either trigger the specific node or trigger some other nodes that are connected to this topic.
- Services: A service is an alternative way of transmitting node data. When applying this process, the system gives priority to the service to be executed while pausing the other operations. 

![2](https://user-images.githubusercontent.com/69988399/102020969-a00fb880-3d8d-11eb-9624-6dcfb01ecfcb.png)

## Packages

To implement this project, you have to install these packages before starting (if you aren’t using [The Construct](https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/) Web Platform. )

[Map_server](http://wiki.ros.org/map_server)

[Gmapping](http://wiki.ros.org/gmapping)

[Amcl](http://wiki.ros.org/amcl)

[Move_base](http://wiki.ros.org/move_base)

[Launch](http://wiki.ros.org/roslaunch)

[Turtlebot3_teleop](https://index.ros.org/p/turtlebot3_teleop/)

[Gazebo_ros_pkgs](http://wiki.ros.org/gazebo_ros_pkgs)

[Turtlebot3_navigation](http://wiki.ros.org/turtlebot3_navigation)



# Tasks Implementation



Before starting any task, we have to create a package first and put all the tasks inside it and that will be by the following commands:
```
cd ~/catkin_ws/src
catkin_create_pkg project_robotics_1 rospy nav_msgs geometry_msgs
cd ~/catkin_ws
catkin_make
source devel/setup.bash
rospack profile
```

## Task 1
The aim of task 1 is to move the robot around the map using a simple /cmd_vel topic and print the range of the robot movement.
### To move the robot and its location, we have to follow some steps:

 1. We have to choose a specific topic and this will be by using “ rostopic list “ and filter it by using command “ | grep “ by the following command:
```
rostopic list | grep /cmd_vel
```
And the results will be:

![2](https://user-images.githubusercontent.com/69988399/102021969-cb49d600-3d94-11eb-83d7-f67cdaf1c800.png)

 2. Choose one of the topics as example “ /cmd_vel “ and get the info of this this topic by using the following command:
```
rostopic info /cmd_vel
```

And the results will be:

![4](https://user-images.githubusercontent.com/69988399/102022070-6642b000-3d95-11eb-88a4-5c0da84b7466.png)

As we see (Type:) is showing the message type that we need it to use the topic publishers and subscribers.
3. The next step is to know the type and the size of Twist message by using the following command:
```
rosmsg show geometry_msgs/twist
```
And the results will be:

![6](https://user-images.githubusercontent.com/69988399/102022073-6773dd00-3d95-11eb-9cd4-6ce046ea4c3f.png)

As we see, there are linear and angular movement and we will use it to move the robot.
5.	We will do the same with the topic “/ odom” as we did with the topic “/cmd_vel”  to get the message type and information as the following figure:

![8](https://user-images.githubusercontent.com/69988399/102023657-2fbd6300-3d9e-11eb-9f24-be5b64e87ef4.JPG)

5. Now we are ready to write our code by using the above information. We will write two python codes, one of a topic publisher that gives the order to move the robot and the other code of a subscriber that get the location of the robot and one launch file. 

•	 At ‘task_1_publish.py’ file, we will create a node and publisher then put the rate and the message values of the movement speed, at the end create a counter variable that makes the robot stop after 30 seconds.

•	 At ‘task_1_subscribe.py’ file, we will create a node and subscriber that get the location information from the topic and print it back by callback function but only the actual coordinates that are changing.

•	 At ‘task_1_move.launch’ file, we will launch the two python files together.

6.	Before launching, we have to compile the packages and execute the bash file that sets the newly generated messages created through the catkin_make by the following commands:
```
roscd; cd ..
catkin_make
source devel/setup.bash
```
7.	The final step to move the robot is to launch the launch-file using the package name and the launch-file name by the following command: 
```
roslaunch project_robotics_1 task_1_move.launch
```
We will see the robot moving according to the values of the msg (linear.x value and
angular.z value) these values is the linear and angular speed of the mobile robot as the following figure.

![WhatsApp Image 2020-12-14 at 1 45 56 AM](https://user-images.githubusercontent.com/69988399/102027981-d57dcb80-3db8-11eb-84d1-26fef8539aee.jpeg)


## Task 2
The aim of this task is to generate the full map of the cafeteria and then localize the Turtlebot3 robot.

In order to approach Task 2 we need to divide the task into sub-processes:
1.	Map generation
2.	Robot localization
### Map generation
For the map generation, we need a specific sequence of processes. First, we need to use the gmapping package in order to run the slam_gmapping node. This node provides the gmapping SLAM algorithm. SLAM generates a 2D map of the robot’s environment during robot the robot’s movement and its laser data info from the /scan topic. This laser data is transformed into OGM data ( Occumaoncy Grid Map) which represents a map with grayscale values that show the map’s status of each pixel (occupied or free).
This is established using:
•	A launch file 
•	A parameter inside the launch file that starts the service of the slam_gmapping node
•	A set of parameters that trigger the laser module and thus the /scan topic.

![10](https://user-images.githubusercontent.com/69988399/102027357-86ce3280-3db4-11eb-8714-619416208773.png)

After executing the gmapping node, we also need to execute an important visualization tool called RVIZ. 
RVIZ is a visualization tool of the robot that provides a lot of visual elements and makes it easier to understand some processes that need visualization. We execute the following command
```
rosrun rviz rviz
```
Thus, after opening the new window, some parameters must be added in order to have a representative perspective identical to the figure below

![12](https://user-images.githubusercontent.com/69988399/102027362-87ff5f80-3db4-11eb-87ab-f3d7528f0a3d.png)

*In the RVIZ menu, the LaserScan must have the (/scan) as topic, the frame element must have the /map topic and the map element must have the /map topic.*

When the whole scan process is completed, the next procedure is to save this map and its parameters by the following command
```
rosrun map_server map_saver -f map_name
```
This command generates the .pgm map and its parameters on a .yaml file.

In the next figure, the .yaml parameters and the .pgm map are generated and the .pgm map depicted.

![13](https://user-images.githubusercontent.com/69988399/102027365-89308c80-3db4-11eb-9bab-4547dd04f66f.png)


### Robot localization
After generating the map, the next procedure is to localize the robot in the generated map. Localization is the process of finding the location of the robot (linear and angular position) inside a map environment. For the purpose of finding these coordinates, we need to use a ROS package called AMCL.

AMCL package provides the Monte Carlo Localization (MCL) algorithm which tracks the localization of a robot moving in a 2D space. In more details, the algorithm generates random poses which are possible guesses of where the robot is. The wrong guesses are discarded, and the correct ones keep on generating. In ROS environment, this process is down by the amcl node.

The amcl node read data from 3 different topics (Subscribe):

 1. The laser topic (/scan) 
 2. The map topic (/map)
 3. The transform topic (/tf)
 
 And transfers the data to 3 other topics (Publish):
 
1.	The amcl_pose topic (/amcl_pose)
2.	The particlecloud topic (/particlecloud)
3.	The transform topic (/tf)

o	/scan: The amcl node gets the scans of the laser data.
o	/map: The amcl node get the map info as OGM for localization
o	/tf: The amcl node uses the relation between of the base_laser and the base_link in order to give the location of the center of the robot.
o	/amcl_pose: The amcl node publishes the robot’s location into the /amcl pose topic.
o	/particlecloud: The amcl node publishes the set of estimated arrows for the robot orientations and localization.

Last step is to perform a global localization approach due to the robustness of localization and the invariance of any visual tool. The steps of applying the localization are provided:

1.	Load the map: 
```
<arg name="map_file" default="$(find project_robotics_1)/maps/ project_1_map_first.yaml"/>
<node name="map_server" pkg="map_server" type="map_server" args="$(arg map_file)" />
```
2.	Call the service particle_client: 
```
<node pkg=" project_robotics_1" type=" particles_script.py" name="service_client" output="screen">
```
3.	Run RVIZ as the next figure

![14](https://user-images.githubusercontent.com/69988399/102027347-79b14380-3db4-11eb-9d86-fd076975049e.png)

In the following figure, the global particle cloud localization is eliminating the wrong estimations and transforms the turtlebot3 and its location to the correct position over time until all the particles acquire the same direction and position along with the robot.  

![15](https://user-images.githubusercontent.com/69988399/102027355-86359c00-3db4-11eb-8e68-95542c819e00.png)


## Task 3

The aim of this task is to set up an automatic system that provides the robot to move from its position to a goal without colliding with any object. 

After generating the map and localizing the robot, the challenge is to move the robot from a position to a goal without colliding with any object. To achieve this, we need to refer to the move_base package. This package and its node (move_base node) aim to move the robot from its current position to a goal position. 

The following figure shows the path planning is initialized step by step. Notify the slight turn of the robot, for the wall avoidance.

![16](https://user-images.githubusercontent.com/69988399/102028329-acf6d100-3dba-11eb-8c72-a88a98bf8697.png)

According to the figure above, the path planning is divided into a compose set of nodes. In order to execute the move_base node, a specific communication among the system components is necessary. The whole move_base node is monitored from a set of specific topics and nodes:

-	The mode_base/goal topic (subscribe): A goal position is provided with execution status.
-	The move_base_simple/goal topic (subscribe): A goal position is provided without giving any status of the execution.
-	The /cmd_vel topic (publish): Velocity publication for robot’s transformation.
-	The move_base/feedback topic: Keeps updating the server for the robot’s information along the path.
-	The move_base/result topic: Information about the robot when it reaches the goal.
-	The Global planner parameter: This parameter builds a non-collision plan for the robot to avoid collisions and obstacles during the goal path. This node plans the path from the whole map is invariant to laser information.
-	The local planner parameter: This parameter builds the path by considering only the sensor data and a small surrounding area of its position at a time in order to plan a path for the goal position.
-	The local costmap parameter: This parameter is responsible for the map’s obstacle information. The local costmap is used for the local planning.
-	The global costmap parameter: This parameter is responsible for the map’s obstacle information. The global costmap is used for the global planning.

In order to move from theory to practice, the launch file that monitors the task 3 approach, consist of a set of different parameter files, launch files and python files for creating the path automatically without establishing any 2D nav goal waypoint from RVIZ. The waypoint was calculated by the topic /get_pose.

The launch file specifically consists of:
1.	Map file, map server.
2.	Amcl file.
3.	Base global planner (NavfnROS).
4.	Base local planner (DWAPlannerROS).
5.	Move base package.
6.	Common costmap parameters.
7.	Global costmap parameters.
8.	Send goal python file.

The following figure shows the map waypoint is initialized for the robot to reach.

![17](https://user-images.githubusercontent.com/69988399/102028324-a8321d00-3dba-11eb-8a7a-1367ba20f858.png)

Running Task 3 and using the RVIZ window panel to see the robot’s path visualization, we first need to adjust some specific parameters, as shown in the figure below.

![18](https://user-images.githubusercontent.com/69988399/102028325-a9634a00-3dba-11eb-8c86-e6f4f4921d66.png)

After adjusting the RVIZ parameters, we can see the robot’s understandable depicted metrics. The map parameter is added two times because the one represents the local costmap and the other map represents the global costmap parameters. The path parameter is initialized with the DWAPlannerROS planner.

Another important file in this approach is the python file. The python file is responsible for monitoring the map’s waypoint with specific coordinates and orientation. Also, the file triggers the turtlebot3’s planner by calling the action server that triggers with its sequence the move_base action client.

![19](https://user-images.githubusercontent.com/69988399/102028326-abc5a400-3dba-11eb-8185-e5c5a3b6364d.png)

Thus, the result is the robot reaching its destination.

![20](https://user-images.githubusercontent.com/69988399/102028327-ac5e3a80-3dba-11eb-99ba-a5a7f35a9e23.png)

## Task 4
The aim of this task is to set up an automatic system that provides the robot to move from its position to a set of waypoints.

The final task corresponds to a set of waypoints instead of one as proposed in Task3. With the same concept as Task3, this challenge can be approached by just increasing the waypoints in the map (see figure below) and the waypoints in the python file. The parameters in RVIZ remain the same. The next figure shows the waypoint initialization is established. The robot must visit these waypoints with the depicted order.

![21](https://user-images.githubusercontent.com/69988399/102028758-cf89e980-3dbc-11eb-9a5f-e3c0d42cbd69.png)

The final image below shows the robot’s ability to maneuver between obstacles without colliding in these three different waypoints.

![22](https://user-images.githubusercontent.com/69988399/102028760-d0bb1680-3dbc-11eb-9d6c-afbc849ca895.png)

# Gant Chart 
The following chart showing the sequence of our work along the whole semester according to the tasks and the number of weeks.

![1111](https://user-images.githubusercontent.com/69988399/102029374-5d66d400-3dbf-11eb-961e-6b1d50c1062f.JPG)

# Conclusion

ROS and its limitless potential of being the most widely used environment in the robotic field, makes it more interesting to computer vision specialist turn into robotic specialists. In this documentation a light introduction of ROS’s possibilities is provided. Turtlebot3 is selected as the protagonist of this project and its capabilities, connections with a plethora of different packages and nodes in order to monitor specific topics and thus generate information. Due to the fact that is python and C++ based, it gives the opportunity to establish from small projects (like this one) to big and unique ones ( eg. Autonomous surgery with use of deep learning and computer vision). As a team we are very interested in working in more challenging tasks in the near future and thus, establish our limitless ideas on a small yet powerful turtlebot3.

# References
  - [WIKI ROS](http://wiki.ros.org/)
  - [The Construct Platform](http://theconstructsim.com)
