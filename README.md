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
## Task 4

