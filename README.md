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

 • Nodes: A node is a built-in ROS function (python, C++) that provides/gets information from ROS topics. ROS nodes can subscribe or publish to a topic for the purpose of sharing important information such as metric values etc.
 •	Topics: A topic is the most important component in the package. It can transmit data between nodes (e.g. one node provides values to the topic, and another node prints the topic’s values) and can provide data throughout ROS built-in sensors, functions etc.
 •	Messages: A message is a data structure provided by a ROS node using a specific topic. These values either trigger the specific node or trigger some other nodes that are connected to this topic.
 • Services: A service is an alternative way of transmitting node data. When applying this process, the system gives priority to the service to be executed while pausing the other operations. 

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
angular.z value) these values are the linear and angular speed of the mobile robot and the location of the robot is being printed every one second.


