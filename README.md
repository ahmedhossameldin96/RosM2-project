<h1 align="center"> ![Capture1](https://user-images.githubusercontent.com/69988399/102021218-49a37980-3d8f-11eb-81e9-2cbe2813c0b0.JPG)

<h1 align="center"> Robotics Project
<h3 align="center"> Supervisors:
<h3 align="center"> Raphael DUVERNE, Daniel BRAUN & Ralph SEULIN
<h3 align="center"> students: 
<h3 align="center"> Vasileios Melissianos and Ahmed Hossameldin











# Introduction
 ROS (Robot Operating System) is one of the best ways to control any robot (mobile robots, robotic arms est..) and that because of ROS is an open-source, meta-operating system. This gives the services you would expect from an operating system, such as abstraction of hardware, low-level device control, widely-used functionality implementation, message-passing between systems, and package management. It also offers tools and libraries on multiple computers to obtain, create, write, and run code.
 
This project is to execute four tasks using TurtleBot 3 mobile robot and simulation performing them on The Construct Web Platform.

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

-	Nodes: A node is a built-in ROS function (python, C++) that provides/gets information from ROS topics. ROS nodes can subscribe or publish to a topic for the purpose of sharing important information such as metric values etc.
-	Topics: A topic is the most important component in the package. It can transmit data between nodes (e.g. one node provides values to the topic, and another node prints the topic’s values) and can provide data throughout ROS built-in sensors, functions etc.
-	Messages: A message is a data structure provided by a ROS node using a specific topic. These values either trigger the specific node or trigger some other nodes that are connected to this topic.
- Services: A service is an alternative way of transmitting node data. When applying this process, the system gives priority to the service to be executed while pausing the other operations. 

![2](https://user-images.githubusercontent.com/69988399/102020969-a00fb880-3d8d-11eb-9624-6dcfb01ecfcb.png)



# Tasks Implementation
## Task 1
The aim of task 1 is to move the robot around the map using a simple /cmd_vel topic and print the range of the robot movement:


